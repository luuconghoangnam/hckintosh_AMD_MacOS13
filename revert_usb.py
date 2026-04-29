import plistlib
import os

def revert_usb(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
        
    with open(path, 'rb') as f:
        pl = plistlib.load(f)
    
    changed = False
    for kext in pl['Kernel']['Add']:
        name = kext['BundlePath']
        if name in ['USBToolBox.kext', 'UTBMap.kext'] and kext['Enabled']:
            kext['Enabled'] = False
            changed = True
            print(f"Disabled {name} in {path}")
        elif name == 'USBMap.kext' and not kext['Enabled']:
            kext['Enabled'] = True
            changed = True
            print(f"Enabled {name} in {path}")
            
    if changed:
        with open(path, 'wb') as f:
            plistlib.dump(pl, f)
            print(f"Saved {path}")

revert_usb('/Users/gonemx/Downloads/USBBootMOS13_Clean/EFI/OC/config.plist')
revert_usb('/Volumes/EFI/EFI/OC/config.plist')
