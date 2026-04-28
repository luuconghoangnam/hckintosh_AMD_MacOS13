import plistlib

def disable_smc_amd(path):
    with open(path, 'rb') as f:
        pl = plistlib.load(f)
    
    changed = False
    for kext in pl['Kernel']['Add']:
        name = kext['BundlePath']
        if name == 'SMCAMDProcessor.kext' and kext['Enabled']:
            kext['Enabled'] = False
            changed = True
            print(f"Disabled {name} in {path}")
            
    if changed:
        with open(path, 'wb') as f:
            plistlib.dump(pl, f)
            print(f"Saved {path}")

disable_smc_amd('/Users/gonemx/Downloads/USBBootMOS13_Clean/EFI/OC/config.plist')
