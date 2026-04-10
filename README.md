# AMD-Hackintosh-MacOS13 (OpenCore EFI)

Bộ OpenCore EFI được tối ưu hóa cho laptop chạy CPU AMD Ryzen 7 5700U (Lucienne) trên macOS 13 Ventura / 14 Sonoma.

---

## 🌟 Giới thiệu

Đây là bộ boot (EFI) hoàn chỉnh giúp cài đặt và vận hành macOS trên các dòng máy sử dụng vi xử lý AMD Ryzen thế hệ 5000 series (Zen 2 Refresh). Bộ EFI này đã được tinh chỉnh để đạt hiệu năng ổn định nhất, hỗ trợ đầy đủ các tính năng cơ bản cho một chiếc laptop.

## 🎯 Tác dụng

- **Hỗ trợ đồ họa**: Kích hoạt Hardware Acceleration cho Integrated Radeon Graphics thông qua `NootedRed.kext`.
- **Tối ưu điện năng**: Quản lý năng lượng CPU ổn định, giúp máy mát và pin bền hơn.
- **Hỗ trợ nhập liệu**: Touchpad hỗ trợ đa điểm (Multi-touch) và Keyboard hoạt động đầy đủ.
- **Kết nối**: Ethernet Realtek hoạt động tốt. (Lưu ý: Wi-Fi tùy thuộc vào card bạn đang dùng).
- **iCloud/App Store**: Đã được thiết lập `NullEthernet` để hỗ trợ đăng nhập các dịch vụ của Apple nếu Wi-Fi không hỗ trợ sẵn.

## 💻 Cấu hình máy chi tiết (Reference)

- **CPU**: AMD Ryzen 7 5700U (8 cores, 16 threads)
- **iGPU**: AMD Radeon Graphics (Renoir/Lucienne)
- **RAM**: 8 GB DDR4
- **SMBIOS**: MacBookPro16,3
- **Bootloader**: OpenCore v0.9.x (hoặc mới hơn)
- **OS Version**: macOS 13.x Ventura (Khuyên dùng) / 14.x Sonoma

## 🛠 Cách dùng (Usage)

### 1. Chuẩn bị
Tải (Clone) repository này về máy:
```bash
git clone https://github.com/luuconghoangnam/AMD-Hackintosh-MacOS13.git
```

### 2. Sanitize & Gen Serial (QUAN TRỌNG)
Bộ EFI này đã được xóa các thông tin Serial (`REPLACEME`). Bạn **CẦN** phải tạo mã định danh mới để sử dụng iMessage/iCloud:
- Mở file `EFI/OC/config.plist` bằng **ProperTree** hoặc **OCAuxiliaryTools**.
- Tìm đến phần `PlatformInfo` -> `Generic`.
- Sử dụng **GenSMBIOS** để tạo mới các trường sau cho model `MacBookPro16,3`:
  - `MLB`
  - `SystemSerialNumber`
  - `SystemUUID`
  - `ROM` (Sử dụng địa chỉ MAC của card mạng)

### 3. Cài đặt
- Copy thư mục `EFI` vào phân vùng EFI của USB Boot hoặc ổ cứng cài macOS.
- Khởi động lại máy và chọn boot từ OpenCore.

## 📝 Chi tiết cấu hình dự án

### Kexts sử dụng:
- `Lilu.kext`: Library hỗ trợ các kext khác.
- `VirtualSMC.kext`: Giả lập chip SMC của Apple.
- `NootedRed.kext`: Driver cho card đồ họa AMD Radeon tích hợp.
- `AppleMCEReporterDisabler.kext`: Ngăn lỗi panic trên CPU AMD.
- `VoodooI2C.kext` & `VoodooPS2Controller.kext`: Hỗ trợ Touchpad và Bàn phím.
- `RealtekRTL8111.kext`: Driver mạng LAN.
- `RestrictEvents.kext`: Sửa lỗi hiển thị thông tin CPU và các dịch vụ khác.

---

### ⚠️ Lưu ý
- Hackintosh là một quá trình thử nghiệm. Tôi không chịu trách nhiệm về bất kỳ hỏng hóc nào liên quan đến phần cứng của bạn.
- Luôn giữ một bản sao lưu (USB Boot) dự phòng trước khi thay đổi EFI trên ổ cứng chính.

---
**Tác giả:** [luuconghoangnam](https://github.com/luuconghoangnam)
**Dự án:** AMD-Hackintosh-MacOS13
