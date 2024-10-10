# BÀI 56: Nhập vào một list số nguyên L, tìm và in ra giá trị dương đầu tiên của list, nếu không có giá trị dương, ta in ra -1
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Tìm giá trị dương đầu tiên trong list
first_positive = -1  # Khởi tạo giá trị mặc định là -1
for num in L:
    if num > 0:
        first_positive = num
        break

# In ra giá trị dương đầu tiên hoặc -1 nếu không có
print(first_positive)
