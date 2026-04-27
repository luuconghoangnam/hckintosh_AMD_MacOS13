import plistlib
import os

in_path = "/Users/gonemx/Downloads/USBBootMOS13_Clean/EFI/OC/Kexts/UTBMap.kext/Contents/Info.plist"
with open(in_path, 'rb') as f:
    pl = plistlib.load(f)

# Native structure
new_pl = {
    "CFBundleDevelopmentRegion": "English",
    "CFBundleIdentifier": "com.corpnewt.USBMap",
    "CFBundleInfoDictionaryVersion": "6.0",
    "CFBundleName": "USBMap",
    "CFBundlePackageType": "KEXT",
    "CFBundleShortVersionString": "1.0",
    "CFBundleSignature": "????",
    "CFBundleVersion": "1.0",
    "IOKitPersonalities": {},
    "OSBundleRequired": "Root"
}

for ctrl_name, ctrl_dict in pl.get("IOKitPersonalities", {}).items():
    native_ctrl = {
        "CFBundleIdentifier": "com.apple.driver.AppleUSBHostMergeProperties",
        "IOClass": "AppleUSBHostMergeProperties",
        "IOMatchCategory": "AppleUSBHostMergeProperties",
        "IOProviderClass": "AppleUSBXHCIPCI",
        "IONameMatch": ctrl_dict.get("IONameMatch", ctrl_name),
        "IOProviderMergeProperties": ctrl_dict.get("IOProviderMergeProperties", {})
    }
    
    # CorpNewt USBMap requires 'model' inside merge properties usually, but it can also just match by IONameMatch directly!
    new_pl["IOKitPersonalities"][f"MacBookPro16,3-{ctrl_name}"] = native_ctrl

out_dir = "/Users/gonemx/Downloads/USBBootMOS13_Clean/EFI/OC/Kexts/USBMap.kext/Contents"
os.makedirs(out_dir, exist_ok=True)
with open(f"{out_dir}/Info.plist", 'wb') as f:
    plistlib.dump(new_pl, f)

print("Created USBMap.kext")
