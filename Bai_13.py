# BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN

# BÀI 13: Nhập vào số nguyên dương a, nếu a lớn hơn 10 thì in ra đây là số lớn hơn 10
a = int(input("Nhập vào số nguyên a: "))
if a > 10:
    print("Đây là số lớn hơn 10.")
else:
    print("Đây là số nhỏ hơn hoặc bằng 10.")

# BÀI 14: Kiểm tra số chẵn hay lẻ
b = int(input("Nhập vào số nguyên b: "))
if b % 2 == 0:
    print("Đây là số chẵn.")
else:
    print("Đây là số lẻ.")

# BÀI 15: Kiểm tra số âm, dương hay bằng 0
c = int(input("Nhập vào số nguyên c: "))
if c > 0:
    print("Đây là số dương.")
elif c < 0:
    print("Đây là số âm.")
else:
    print("Đây là số 0.")

# BÀI 16: Kiểm tra số nguyên d có chia hết cho 5 hay không
d = int(input("Nhập vào số nguyên d: "))
if d % 5 == 0:
    print("Số này chia hết cho 5.")
else:
    print("Số này không chia hết cho 5.")