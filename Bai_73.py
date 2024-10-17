# BÀI 73: Viết hàm đưa vào 2 số nguyên, số nào lớn hơn thì in bảng cửu chương của số đó
def print_multiplication_table(a, b):
    # Tìm số lớn hơn
    larger = max(a, b)

    # In bảng cửu chương của số lớn hơn
    print(f"Bảng cửu chương của {larger}:")
    for i in range(1, 11):  # Từ 1 đến 10
        print(f"{larger} x {i} = {larger * i}")

# Nhập vào hai số nguyên
num1 = int(input("Nhập số nguyên thứ nhất: "))
num2 = int(input("Nhập số nguyên thứ hai: "))

# Gọi hàm để in bảng cửu chương
print_multiplication_table(num1, num2)