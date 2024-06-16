# Đọc giá trị đầu vào
f = int(input())  # Số lít nhiên liệu ban đầu
d = int(input())  # Quãng đường cần đi tính bằng mét
r = int(input())  # Tốc độ tiêu thụ nhiên liệu tính bằng lít/mét

# Tính toán số lít nhiên liệu cần thiết
fuel_needed = d * r

# Kiểm tra xem nhiên liệu ban đầu có đủ không
if f >= fuel_needed:
    remaining_fuel = f - fuel_needed
    print(remaining_fuel)
else:
    print("not enough fuel")
