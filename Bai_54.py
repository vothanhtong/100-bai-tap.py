# BÀI 54: Nhập vào một list số nguyên L, nhập vào 2 số nguyên dương a và b (a < b < len(L))
# Tìm và in ra số nhỏ nhất trong list từ vị trí a đến vị trí b
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Nhập hai số nguyên dương a và b (a < b < len(L))
a = int(input("Nhập số nguyên a (a < b < len(L)): "))
b = int(input("Nhập số nguyên b (a < b < len(L)): "))

# Kiểm tra điều kiện a < b < len(L)
if 0 <= a < b < len(L):
    # Tìm giá trị nhỏ nhất trong đoạn từ vị trí a đến vị trí b
    min_value = min(L[a:b+1])
    print(f"Giá trị nhỏ nhất từ vị trí {a} đến vị trí {b} trong list là:", min_value)
else:
    print("Giá trị a và b không hợp lệ.")