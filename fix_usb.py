import plistlib

def patch_plist(path):
    with open(path, 'rb') as f:
        pl = plistlib.load(f)
    
    changed = False
    for kext in pl['Kernel']['Add']:
        name = kext['BundlePath']
        if name == 'USBMap.kext' and kext['Enabled']:
            kext['Enabled'] = False
            changed = True
            print(f"Disabled {name} in {path}")
        elif name in ['USBToolBox.kext', 'UTBMap.kext'] and not kext['Enabled']:
            kext['Enabled'] = True
            changed = True
            print(f"Enabled {name} in {path}")
            
    if changed:
        with open(path, 'wb') as f:
            plistlib.dump(pl, f)
            print(f"Saved {path}")

patch_plist('/Volumes/EFI/EFI/OC/config.plist')
patch_plist('/Users/gonemx/Downloads/USBBootMOS13_Clean/EFI/OC/config.plist')
