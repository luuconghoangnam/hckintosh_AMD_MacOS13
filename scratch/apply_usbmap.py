import plistlib
import shutil

for plist_path in ["/Users/gonemx/Downloads/USBBootMOS13_Clean/EFI/OC/config.plist", "/Volumes/EFI/EFI/OC/config.plist"]:
    try:
        with open(plist_path, 'rb') as f:
            pl = plistlib.load(f)

        kernel_add = pl.get('Kernel', {}).get('Add', [])
        
        # Disable old
        for k in kernel_add:
            if k['BundlePath'] in ['USBToolBox.kext', 'UTBMap.kext']:
                k['Enabled'] = False
        
        # Add USBMap
        has_usbmap = any(k['BundlePath'] == 'USBMap.kext' for k in kernel_add)
        if not has_usbmap:
            kernel_add.append({
                'Arch': 'Any',
                'BundlePath': 'USBMap.kext',
                'Comment': 'USBMap.kext Native',
                'Enabled': True,
                'ExecutablePath': '',
                'MaxKernel': '',
                'MinKernel': '',
                'PlistPath': 'Contents/Info.plist',
            })
        else:
            for k in kernel_add:
                if k['BundlePath'] == 'USBMap.kext':
                    k['Enabled'] = True

        with open(plist_path, 'wb') as f:
            plistlib.dump(pl, f)
            
        print(f"Updated {plist_path}")
    except Exception as e:
        print(f"Failed {plist_path}: {e}")

