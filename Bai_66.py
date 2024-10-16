# BÀI 66 : Nhập vào một list số nguyên L, hãy đếm số lượng giá trị trong list thỏa tính chất: “lớn hơn tất cả các giá trị đứng đằng trước nó”
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Biến để đếm số lượng giá trị thỏa mãn
count = 0

# Biến để lưu giá trị lớn nhất đã gặp trước đó
max_value = float('-inf')  # Khởi tạo là âm vô cực

# Duyệt qua từng phần tử trong list
for num in L:
    if num > max_value:
        count += 1  # Tăng số lượng nếu num lớn hơn giá trị lớn nhất trước đó
        max_value = num  # Cập nhật giá trị lớn nhất

# In ra kết quả
print("Số lượng giá trị thỏa tính chất là:", count)