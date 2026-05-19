#!/bin/bash

# Script to hacktivate (Skip Setup) for Dead Baseband iPhone
# Requirement: iproxy (brew install libimobiledevice)

PORT=2222
PASS="alpine"

echo "[*] Đang khởi chạy iproxy trên cổng $PORT..."
iproxy $PORT 22 > /dev/null 2>&1 &
IPROXY_PID=$!

echo "[*] Đang đợi kết nối SSH (đảm bảo máy đã jailbreak và ở màn hình Hello)..."

while ! nc -z 127.0.0.1 $PORT; do
  sleep 2
done

echo "[+] Đã kết nối được cổng $PORT. Chờ 5s để dịch vụ SSH ổn định..."
sleep 5

echo "[+] Bắt đầu thực thi lệnh qua SSH..."

# Execute hacktivation commands
sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p $PORT root@127.0.0.1 << 'EOF'
    echo "[*] Đang mount lại phân vùng hệ thống..."
    mount -o rw,remount /
    
    if [ -d "/Applications/Setup.app" ]; then
        echo "[*] Đang ẩn Setup.app (Bypass Activation)..."
        mv /Applications/Setup.app /Applications/Setup.app.bak
        echo "[*] Đang làm mới cache ứng dụng..."
        uicache -a
        echo "[*] Đang khởi động lại giao diện (Respring)..."
        killall backboardd
        echo "[+] Hoàn tất! Điện thoại sẽ vào màn hình chính."
    else
        echo "[!] Không tìm thấy Setup.app. Có thể đã được bypass hoặc lỗi mount."
    fi
EOF

# Cleanup
kill $IPROXY_PID
echo "[*] Đã đóng iproxy."
