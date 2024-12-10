#!/bin/bash
#
# SPDX-FileCopyrightText: 2016 The CyanogenMod Project
# SPDX-FileCopyrightText: 2017-2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

function blob_fixup() {
    case "${1}" in
        vendor/lib/libswregistrationalgo.so)
            [ "$2" = "" ] && return 0
            ${PATCHELF} --replace-needed "libprotobuf-cpp-full.so" "libprotobuf-cpp-full-v29.so" "${2}"
            ;;
        vendor/lib/libBlendScreen.so \
        | vendor/lib/libGetExposureValue.so \
        | vendor/lib/libHDRI.so \
        | vendor/lib/libManis.so \
        | vendor/lib/libmeitucapture.so \
        | vendor/lib/libMeituColorSystem3DLut.so \
        | vendor/lib/libMeituColorSystem.so \
        | vendor/lib/libMeituDeBlur.so \
        | vendor/lib/libMeituDefocus.so \
        | vendor/lib/libmlabmakeup.so \
        | vendor/lib/libmtbodycontour.so \
        | vendor/lib/libMTChromaNR.so \
        | vendor/lib/libmtCLUtil.so \
        | vendor/lib/libmtColorNoiseFilter.so \
        | vendor/lib/libmtface.so \
        | vendor/lib/libmtmakeupInterface.so \
        | vendor/lib/libmtMultiFrameDenoise.so \
        | vendor/lib/libmtnn.so \
        | vendor/lib/libmtphotosegment.so \
        | vendor/lib/libMTSkin.so \
        | vendor/lib/libmtvenom.so \
        | vendor/lib/liborb.so \
        | vendor/lib/libPathBlur.so)
            [ "$2" = "" ] && return 0
            "${PATCHELF_0_17_2}" --replace-needed "libstdc++.so" "libstdc++_vendor.so" "${2}"
            ;;
        *)
            return 1
            ;;
    esac

    return 0
}

function blob_fixup_dry() {
    blob_fixup "$1" ""
}

# If we're being sourced by the common script that we called,
# stop right here. No need to go down the rabbit hole.
if [ "${BASH_SOURCE[0]}" != "${0}" ]; then
    return
fi

set -e

export DEVICE=vela
export DEVICE_COMMON=sdm710-common
export VENDOR=xiaomi
export VENDOR_COMMON=${VENDOR}

"./../../${VENDOR_COMMON}/${DEVICE_COMMON}/extract-files.sh" "$@"
