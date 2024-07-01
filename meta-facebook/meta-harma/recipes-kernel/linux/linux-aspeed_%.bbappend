FILESEXTRAPATHS:prepend := "${THISDIR}/linux-aspeed:"

SRC_URI:append = " file://1000-ARM-dts-aspeed-Harma-Revise-node-name.patch"
SRC_URI:append = " file://1001-ARM-dts-aspeed-Harma-Add-retimer-device.patch"
SRC_URI:append = " file://1002-ARM-dts-aspeed-Harma-Modify-GPIO-line-name.patch"
SRC_URI:append = " file://1003-ARM-dts-aspeed-Harma-revise-hsc-chip.patch"
SRC_URI:append = " file://1004-ARM-dts-aspeed-Harma-add-VR-device.patch"
SRC_URI:append = " file://1005-ARM-dts-aspeed-Harma-add-sgpio-name.patch"
SRC_URI:append = " file://1006-ARM-dts-aspeed-Harma-add-ina238.patch"
SRC_URI:append = " file://1007-ARM-dts-aspeed-Harma-add-power-monitor-xdp710.patch"
SRC_URI:append = " file://1008-ARM-dts-aspeed-Harma-remove-multi-host-property.patch"
SRC_URI:append = " file://1009-ARM-dts-aspeed-Harma-add-fru-device.patch"
SRC_URI:append = " file://1010-ARM-dts-aspeed-Harma-add-temperature-device.patch"
SRC_URI:append = " file://1011-ARM-dts-aspeed-Harma-enable-mctp-controller.patch"
SRC_URI:append = " file://1012-ARM-dts-aspeed-Harma-add-lpc_pcc-device.patch"
SRC_URI:append = " file://1013-ARM-dts-aspeed-Harma-stop-NIC-run-time-polling.patch"
SRC_URI:append = " file://1014-ARM-dts-aspeed-Harma-read-cpu-temp-and-power.patch"
