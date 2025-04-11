# BÀI 11: Nhập vào 3 số a, b, c. In ra kết quả là tổng của ba số đó
a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
tong = a + b + c
print("Tổng ba số a, b, c là: ", tong)

# Ví dụ minh họa:
# Nhập vào số nguyên a: 5
# Nhập vào số nguyên b: 10
# Nhập vào số nguyên c: 15
# Tổng ba số a, b, c là: 30

## BÀI: In bảng cửu chương không trùng lặp
def print_multiplication_table():
    for i in range(1, 10):  # Duyệt từ 1 đến 9
        for j in range(i, 10):  # Duyệt từ i đến 9 để tránh trùng lặp
            print(f"{i} x {j} = {i * j}")
    print("Bảng cửu chương không trùng lặp đã được in ra.")

# Gọi hàm để in bảng cửu chương
print_multiplication_table()

# Ví dụ minh họa:
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 9 x 9 = 81
# Bảng cửu chương không trùng lặp đã được in ra.