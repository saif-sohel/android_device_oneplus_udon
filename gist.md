# Fixing nsjail Sandbox Errors in AOSP Builds on Ubuntu 24.04/24.10

When setting up an AOSP build environment on Ubuntu 24.04/24.10, you might encounter the following error when running the `lunch` command:
```
Build sandboxing disabled due to nsjail error.
```

This issue is related to AppArmor restrictions on unprivileged user namespaces, which were introduced in Ubuntu 24.04 and affect the nsjail tool used by the AOSP build system.

## Solution: Create a Custom AppArmor Profile for nsjail

### Step 1: Create the AppArmor Profile

Create a new AppArmor profile file specifically for nsjail:

```bash
sudo nano /etc/apparmor.d/home.nsjail
```

### Step 2. Add the proper variable declaration and profile:

```
#include <tunables/global>

profile home.nsjail /home/*/*/prebuilts/build-tools/linux-x86/bin/nsjail flags=(unconfined) {
}
```
Replace "/home/" with the appropriate directory if needed.

### Step 3. Load the updated profile:

```bash
sudo apparmor_parser -r /etc/apparmor.d/home.nsjail
```
