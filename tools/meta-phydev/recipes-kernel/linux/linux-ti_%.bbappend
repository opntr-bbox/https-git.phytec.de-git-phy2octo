#SRC_URI = "git://git@git.phytec.de/linux-ti;protocol=ssh;branch=${BRANCH}"
SRC_URI = "git://${HOME}/linux-ti;protocol=file;branch=${BRANCH}"
#SRC_URI_append = " file://remove-cm3-firmware.cfg"

#BRANCH_phyflex-am335x-1 = "3.12.24-phy"

do_deploy_append () {
    if [ ${DEV_BUILD} == "True" ]; then
        bbnote "Deploying linuximage and oftree to ${TFTP_ROOT}"
        install -m 777 ${KERNEL_OUTPUT} ${TFTP_ROOT}/${DEV_USER}-linux-${MACHINE}
        install -m 777 ${DTB_PATH} ${TFTP_ROOT}/${DEV_USER}-oftree-${MACHINE}
    fi
}


