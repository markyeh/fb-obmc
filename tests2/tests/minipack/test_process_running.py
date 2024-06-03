#!/usr/bin/env python3
#
# Copyright 2018-present Facebook. All Rights Reserved.
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
import unittest

from common.base_process_running_test import BaseProcessRunningTest
from utils.test_utils import qemu_check, running_systemd


class ProcessRunningTest(BaseProcessRunningTest, unittest.TestCase):
    def set_processes(self):
        self.expected_process = [
            "front-paneld",
            "ipmbd",
            "ipmid",
            "mTerm_server",
            "rest.py",
            "restapi",
            "sensord",
            "rsyslogd",
            "usbmon.sh",
        ]
        SYSV_PROCESSES = [
            "dhclient -6 -d -D LL",
            "dhclient -pf /var/run/dhclient.eth0.pid eth0",
        ]
        SYSTEMD_PROCESSES = [
            "systemd-journald",
            "systemd-udevd",
            "systemd-resolved",
            "systemd-timesyncd",
            "systemd-networkd",
        ]
        self.expected_process.extend(
            SYSTEMD_PROCESSES if running_systemd() else SYSV_PROCESSES
        )
        if not qemu_check():
            self.expected_process.extend(["fscd"])
