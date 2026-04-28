import plistlib

def fix_bt_order(path):
    with open(path, 'rb') as f:
        pl = plistlib.load(f)
    
    kernel_add = pl['Kernel']['Add']
    
    # Find and extract the three kexts
    firmware_kext = None
    patcher_kext = None
    fixup_kext = None
    
    new_add = []
    for kext in kernel_add:
        name = kext['BundlePath']
        if name == 'IntelBluetoothFirmware.kext':
            firmware_kext = kext
        elif name == 'IntelBTPatcher.kext':
            patcher_kext = kext
        elif name == 'BlueToolFixup.kext':
            fixup_kext = kext
        else:
            new_add.append(kext)
            
    # Add them back in the correct order
    if firmware_kext:
        new_add.append(firmware_kext)
    if patcher_kext:
        new_add.append(patcher_kext)
    if fixup_kext:
        new_add.append(fixup_kext)
        
    pl['Kernel']['Add'] = new_add
    
    with open(path, 'wb') as f:
        plistlib.dump(pl, f)
        print(f"Fixed Bluetooth loading order in {path}")

fix_bt_order('/Users/gonemx/Downloads/USBBootMOS13_Clean/EFI/OC/config.plist')
