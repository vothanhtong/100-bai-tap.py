# BÀI TẬP NHẬP LIỆU VÀ TOÁN TỬ CƠ BẢN
# BÀI 1: Nhập vào số n, hãy nhân n lên cho 3, rồi cộng 1 sau đó in kết quả ra màn hình
a=int(input("nhập vào số nguyên a: "))
n=(a*3)+1
print("khi a nhân cho ba và cộng cho một là: ",n)

# BÀI 2: Nhập vào hai số nguyên a và b, tính tổng, hiệu, tích, thương của chúng
a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b if b != 0 else "Không thể chia cho 0"
print("Tổng của a và b là:", tong)
print("Hiệu của a và b là:", hieu)
print("Tích của a và b là:", tich)
print("Thương của a và b là:", thuong)

# BÀI 3: Nhập vào bán kính r của hình tròn, tính diện tích và chu vi
import math
r = float(input("Nhập vào bán kính r: "))
chu_vi = 2 * math.pi * r
dien_tich = math.pi * r ** 2
print("Chu vi hình tròn là:", chu_vi)
print("Diện tích hình tròn là:", dien_tich)

# BÀI 4: Nhập vào một số nguyên n, kiểm tra xem n là số chẵn hay lẻ
n = int(input("Nhập vào số nguyên n: "))
if n % 2 == 0:
    print(f"{n} là số chẵn.")
else:
    print(f"{n} là số lẻ.")

# BÀI 5: Nhập vào một số nguyên n, tính n bình phương
n = int(input("Nhập vào số nguyên n: "))
binh_phuong = n ** 2
print(f"Bình phương của {n} là: {binh_phuong}")