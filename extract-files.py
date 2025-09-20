#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/qcom-caf/sdm845',
    'hardware/xiaomi',
    'vendor/xiaomi/sdm710-common',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/lib/hw/com.qti.chi.override.so': blob_fixup()
        .binary_regex_replace(b'persist.vendor.camera.xiaomi.remapid',
                              b'vendor.camera.remapid\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),
    (
        'vendor/lib/libBlendScreen.so',
        'vendor/lib/libGetExposureValue.so',
        'vendor/lib/libHDRI.so',
        'vendor/lib/libManis.so',
        'vendor/lib/libmeitucapture.so',
        'vendor/lib/libMeituColorSystem3DLut.so',
        'vendor/lib/libMeituColorSystem.so',
        'vendor/lib/libMeituDeBlur.so',
        'vendor/lib/libMeituDefocus.so',
        'vendor/lib/libmlabmakeup.so',
        'vendor/lib/libmtbodycontour.so',
        'vendor/lib/libMTChromaNR.so',
        'vendor/lib/libmtCLUtil.so',
        'vendor/lib/libmtColorNoiseFilter.so',
        'vendor/lib/libmtface.so',
        'vendor/lib/libmtmakeupInterface.so',
        'vendor/lib/libmtMultiFrameDenoise.so',
        'vendor/lib/libmtnn.so',
        'vendor/lib/libmtphotosegment.so',
        'vendor/lib/libMTSkin.so',
        'vendor/lib/libmtvenom.so',
        'vendor/lib/liborb.so',
        'vendor/lib/libPathBlur.so',
    ): blob_fixup().replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'vela',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'sdm710-common', module.vendor)
    utils.run()
