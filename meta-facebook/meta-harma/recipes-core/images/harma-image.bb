require common/images/fb-openbmc-image.inc

# Install temporary firmware update utilities, retimer-util and apml debug tools for POC phase.
IMAGE_INSTALL:append = " fw-util"
IMAGE_INSTALL:append = " apml"
IMAGE_INSTALL:append = " retimer-util"
IMAGE_INSTALL:append = " system-state-init"
IMAGE_INSTALL:append = " pldm-update"
IMAGE_INSTALL:append = " compute-software-id"
IMAGE_INSTALL:append = " dimm-util"
IMAGE_INSTALL:append = " cpld-fw-handler"
