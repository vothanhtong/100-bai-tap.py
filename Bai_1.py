# BÀI 1: Nhập vào số n, nhân n lên cho 3, rồi cộng 1
a = int(input("Nhập vào số nguyên a: "))
print("Kết quả:", (a * 3) + 1)

# BÀI 2: Nhập hai số nguyên a và b, tính tổng, hiệu, tích, thương
a, b = map(int, input("Nhập hai số nguyên a và b, cách nhau bởi khoảng trắng: ").split())
print(f"Tổng: {a + b}, Hiệu: {a - b}, Tích: {a * b}, Thương: {a / b if b != 0 else 'Không thể chia cho 0'}")

# BÀI 3: Nhập bán kính r, tính diện tích và chu vi hình tròn
import math
r = float(input("Nhập bán kính r: "))
print(f"Chu vi: {2 * math.pi * r}, Diện tích: {math.pi * r ** 2}")

# BÀI 4: Nhập số nguyên n, kiểm tra chẵn hay lẻ
n = int(input("Nhập số nguyên n: "))
print(f"{n} là số {'chẵn' if n % 2 == 0 else 'lẻ'}.")

# BÀI 5: Nhập số nguyên n, tính bình phương
n = int(input("Nhập số nguyên n: "))
print(f"Bình phương của {n} là: {n ** 2}")