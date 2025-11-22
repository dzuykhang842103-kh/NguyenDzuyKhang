import socket # Thư viện để kết nối mạng
from datetime import datetime # Thư viện để lấy giờ hiện tại

# 1. Xác định mục tiêu quét
# Chúng ta sẽ quét chính máy tính của mình (localhost) để an toàn
target = "127.0.0.1" 

print("-" * 50)
print(f"Đang quét mục tiêu: {target}")
print(f"Thời gian bắt đầu: {datetime.now()}")
print("-" * 50)

try:
    # 2. Quét các cổng từ 1 đến 100 (Các cổng phổ biến)
    for port in range(1, 100): 
        # Tạo một socket (giống như tạo một cái điện thoại để gọi)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Thiết lập thời gian chờ (timeout) là 1 giây
        # Nếu quá 1 giây không ai trả lời thì bỏ qua
        socket.setdefaulttimeout(1)
        
        # 3. Thử kết nối tới cổng (Đây là hành động gõ cửa)
        # Hàm connect_ex trả về 0 nghĩa là Cổng Đang Mở (Có người mở cửa)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Phát hiện cổng {port} đang MỞ")
        
        # Đóng kết nối sau khi kiểm tra xong
        s.close()

except KeyboardInterrupt:
    print("\nĐã dừng quét!")
except socket.error:
    print("\nKhông kết nối được đến máy chủ.")

print("-" * 50)
print("Hoàn thành quét port.")