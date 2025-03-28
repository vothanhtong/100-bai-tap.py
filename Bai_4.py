# BÀI 4:Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False
a=int(input("nhập vào số nguyên a: "))
if a%2==0:
    print("TRUE")
else:
    print("FALSE")

# Bài 4.1 nhập vào số nguyên a chia hết cho 3 thì in ra True, ngược lại in ra Fale 
a = int(input("nhập số nguyên a :"))
if a % 3 == 0:
    print("TRUE")
else:
    print("Fale")

# Bài 4.2 nhập số nguyên a chia hết cho 5 
a = int(input("nhập số bguyeen bất kỳ"))
if a % 5 == 0:
    print("true")
else:
    print("fale")

# Bài 4.3: Nhập một số bất kỳ, kiểm tra xem là số âm, số dương hay số thập phân
a = input("Nhập một số bất kỳ: ")
try:
    a = float(a)  # Chuyển đổi sang kiểu float để kiểm tra số thập phân
    if a < 0:
        print("Đây là số âm.")
    elif a > 0:
        print("Đây là số dương.")
    if a % 1 != 0:
        print("Đây là số thập phân.")
    else:
        print("Đây là số nguyên.")
except ValueError:
    print("Đây không phải là một số hợp lệ.")