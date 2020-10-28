#!/bin/sh
#
# Copyright 2020-present Facebook. All Rights Reserved.
#
# This program file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program in a file named COPYING; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#
# This tool is used to setup the SPI mux on the PIM from connecting to DOM FPGA to connecting to IOB FPGA,
# so that IOB FPGA has the ability to read and write Flash on PIM.
# Before updating the DOM FPGA, we must set the SPI mux of PIM to access the Flash of DOM FPGA.
#

set_pca9534_register(){

    register=$1
    value=$2

    # Set IOB FPGA indirect Access Address 0x00001500
    i2cset -y -f 13 0x35 0xf0 0x00 0x00 0x15 0x00 i
    # Set IOB FPGA Write Data 0x0000fc03
    i2cset -y -f 13 0x35 0xf4 0x00 0x00 "$value" "$register" i

    # Set Command Write Action
    i2cset -y -f 13 0x35 0xfc 0x1 b
}

flush_ucd_register(){

    # Set IOB FPGA indirect Access Address 0x0000148c
    i2cset -y -f 13 0x35 0xf0 0x00 0x00 0x14 0x8c i
    # Set IOB FPGA Write Data 0x00000003
    i2cset -y -f 13 0x35 0xf4 0x00 0x00 0x00 0x03 i

    # Set Command Write Action
    i2cset -y -f 13 0x35 0xfc 0x1

    # Set IOB FPGA indirect Access Address 0x00001484
    i2cset -y -f 13 0x35 0xf0 0x00 0x00 0x14 0x84 i
    # Set IOB FPGA Write Data 0x80220200
    i2cset -y -f 13 0x35 0xf4 0x80 0x22 0x02 0x00 i

    # Set Command Write Action
    i2cset -y -f 13 0x35 0xfc 0x1
}

setup_pims_switch_mux(){

    flush_ucd_register

    # Register 3 -  Configuration Register
    set_pca9534_register "0x03" "0xc0"

    flush_ucd_register

    #
    # Set Register 1 - Output Port Register bit[1] - O1
    #
    # Register 1 -  Output Port Register
    set_pca9534_register "0x01" "0xd5"

    flush_ucd_register
}

echo 0x06 > /sys/bus/i2c/devices/12-003e/spi1_sel

for i in 0 1 2 3 4 5 6 7
do
    cmd=$(printf "i2cset -y -f 13 0x35 0x76 0x%02x 0x%02x i\n" "$(((i+8)<<4))" "$((1<<i))")
    $cmd
    setup_pims_switch_mux
done

