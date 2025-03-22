#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/oneplus/sm8450-common',
]

# Device-specific blob fixups, if any
blob_fixups: blob_fixups_user_type = {
}

module = ExtractUtilsModule(
    'udon',  # device codename
    'oneplus',  # vendor
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    check_elf=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8450-common', module.vendor
    )
    utils.run()