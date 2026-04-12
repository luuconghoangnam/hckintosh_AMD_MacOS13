import plistlib

def update_config(plist_path):
    with open(plist_path, 'rb') as f:
        pl = plistlib.load(f)

    kernel_add = pl.get('Kernel', {}).get('Add', [])
    kext_names = {k['BundlePath'] for k in kernel_add}

    # New kexts to add
    new_kexts = [
        {
            'Arch': 'Any',
            'BundlePath': 'AirportItlwm.kext',
            'Comment': 'AirportItlwm.kext',
            'Enabled': True,
            'ExecutablePath': 'Contents/MacOS/AirportItlwm',
            'MaxKernel': '',
            'MinKernel': '',
            'PlistPath': 'Contents/Info.plist',
        },
        {
            'Arch': 'Any',
            'BundlePath': 'IntelBluetoothFirmware.kext',
            'Comment': 'IntelBluetoothFirmware.kext',
            'Enabled': True,
            'ExecutablePath': 'Contents/MacOS/IntelBluetoothFirmware',
            'MaxKernel': '',
            'MinKernel': '',
            'PlistPath': 'Contents/Info.plist',
        }
    ]

    for nk in new_kexts:
        if nk['BundlePath'] not in kext_names:
            kernel_add.append(nk)
            print(f"Added {nk['BundlePath']}")
        else:
            # If already there, ensure it's enabled
            for k in kernel_add:
                if k['BundlePath'] == nk['BundlePath']:
                    k['Enabled'] = True
                    print(f"Enabled {nk['BundlePath']}")

    # Enable specific existing kexts
    to_enable = {
        'IntelBTPatcher.kext',
        'BlueToolFixup.kext',
        'USBToolBox.kext',
        'UTBMap.kext'
    }

    for k in kernel_add:
        if k['BundlePath'] in to_enable:
            k['Enabled'] = True
            print(f"Enabled {k['BundlePath']}")

    with open(plist_path, 'wb') as f:
        plistlib.dump(pl, f)

if __name__ == "__main__":
    update_config("/Volumes/EFI/EFI/OC/config.plist")
