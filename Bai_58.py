# BÀI 58:Nhập vào một list số nguyên L, nhập vào số nguyên x, tìm giá trị trong list xa x nhất
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Nhập vào số nguyên x
x = int(input("Nhập số nguyên x: "))

# Tìm giá trị trong list xa x nhất
max_diff = -1  # Khởi tạo khoảng cách lớn nhất
result = None  # Giá trị xa x nhất

for num in L:
    diff = abs(num - x)  # Tính khoảng cách tuyệt đối giữa num và x
    if diff > max_diff:
        max_diff = diff
        result = num

# In ra giá trị xa x nhất
print("Giá trị xa x nhất là:", result)