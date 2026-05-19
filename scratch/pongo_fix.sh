#!/bin/bash

# Script to fix PongoOS hang by sending manual boot command
# Requirement: brew install libirecovery

echo "[*] Đang đợi thiết bị ở chế độ PongoOS..."

while true; do
    # Check if device is in Pongo mode
    MODE=$(irecovery -m 2>/dev/null | grep -o "Pongo")
    
    if [ "$MODE" == "Pongo" ]; then
        echo "[+] Đã tìm thấy thiết bị ở chế độ PongoOS!"
        echo "[*] Đang gửi lệnh boot..."
        irecovery -c boot
        echo "[!] Đã gửi lệnh boot. Vui lòng kiểm tra điện thoại."
        break
    fi
    sleep 1
done
