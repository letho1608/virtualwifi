import subprocess
import time

def create_virtual_wifi(ssid):
    # Bật chế độ phát Wi-Fi ảo
    subprocess.call("netsh wlan set hostednetwork mode=allow ssid={} key=".format(ssid), shell=True)

    # Bắt đầu phát Wi-Fi ảo
    subprocess.call("netsh wlan start hostednetwork", shell=True)

    print("Đã tạo điểm truy cập Wi-Fi ảo với tên mạng: " + ssid)

def enable_virtual_wifi():
    while True:
        time.sleep(1)
        print("Chương trình đang chạy. Thiết bị khác có thể tìm thấy các điểm truy cập Wi-Fi ảo.")

try:
    num_networks = int(input("Nhập số lượng điểm truy cập Wi-Fi ảo: "))
    for i in range(num_networks):
        ssid = "VirtualWiFi_" + str(i+1)
        create_virtual_wifi(ssid)

    enable_virtual_wifi()

except KeyboardInterrupt:
    # Tắt điểm truy cập Wi-Fi ảo trước khi thoát chương trình
    subprocess.call("netsh wlan stop hostednetwork", shell=True)
    print("\nChương trình đã được dừng.")
