# BÀI TẬP VÒNG LẶP FOR
# BÀI  23: In 10 lần chữ hello ra màn hình
for i in range (1,10+1):
    print("In 10 lần chữ hello ra màn hình")

    # BÀI TẬP VÒNG LẶP FOR
# BÀI 23: In 10 lần chữ hello ra màn hình
for i in range(1, 10 + 1):
    print("In 10 lần chữ hello ra màn hình")

# BÀI 23.1: In các số từ 1 đến 10
print("\nBÀI 23.1: In các số từ 1 đến 10")
for i in range(1, 11):
    print(i)

# BÀI 23.2: In các số chẵn từ 2 đến 20
print("\nBÀI 23.2: In các số chẵn từ 2 đến 20")
for i in range(2, 21, 2):
    print(i)

# BÀI 23.3: In các số lẻ từ 1 đến 19
print("\nBÀI 23.3: In các số lẻ từ 1 đến 19")
for i in range(1, 20, 2):
    print(i)

# BÀI 23.4: In bảng cửu chương 5
print("\nBÀI 23.4: In bảng cửu chương 5")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
    
    # vong_lap_for.py
# TỔNG HỢP CÁC BÀI TẬP VÒNG LẶP FOR TRONG PYTHON

# --------------------------
# Bài 23: In 10 lần chữ "hello"
# --------------------------
print("Bài 23: In 10 lần chữ 'hello'")
for i in range(10):
    print("Hello")

# --------------------------
# Bài 23.1: In các số từ 1 đến 10
# --------------------------
print("\nBài 23.1: In các số từ 1 đến 10")
for i in range(1, 11):
    print(i)

# --------------------------
# Bài 23.2: In các số chẵn từ 2 đến 20
# --------------------------
print("\nBài 23.2: In các số chẵn từ 2 đến 20")
for i in range(2, 21, 2):
    print(i)

# --------------------------
# Bài 23.3: In các số lẻ từ 1 đến 19
# --------------------------
print("\nBài 23.3: In các số lẻ từ 1 đến 19")
for i in range(1, 20, 2):
    print(i)

# --------------------------
# Bài 23.4: In bảng cửu chương 5
# --------------------------
print("\nBài 23.4: In bảng cửu chương 5")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# --------------------------
# Bài 23.5: Tính tổng các số từ 1 đến 100
# --------------------------
print("\nBài 23.5: Tính tổng các số từ 1 đến 100")
tong = 0
for i in range(1, 101):
    tong += i
print("Tổng từ 1 đến 100 là:", tong)

# --------------------------
# Bài 23.6: Đếm ngược từ 10 đến 1
# --------------------------
print("\nBài 23.6: Đếm ngược từ 10 đến 1")
for i in range(10, 0, -1):
    print(i)

# --------------------------
# Bài 23.7: In bảng cửu chương từ 1 đến 9
# --------------------------
print("\nBài 23.7: In bảng cửu chương từ 1 đến 9")
for i in range(1, 10):
    print(f"\nBảng cửu chương {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

# --------------------------
# Bài 23.8: In các số chia hết cho 3 từ 1 đến 50
# --------------------------
print("\nBài 23.8: In các số chia hết cho 3 từ 1 đến 50")
for i in range(1, 51):
    if i % 3 == 0:
        print(i)

# --------------------------
# Bài 23.9: Kiểm tra số nguyên tố
# --------------------------
print("\nBài 23.9: Kiểm tra số nguyên tố")
n = int(input("Nhập số nguyên dương: "))
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")

# --------------------------
# Bài 23.10: In hình tam giác sao
# --------------------------
print("\nBài 23.10: In hình tam giác sao")
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
