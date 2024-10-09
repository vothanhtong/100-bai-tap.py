# BÀI TẬP XỬ LÝ LIST
# BÀI 53: Nhập vào list số nguyên
# Nhập vào một list số nguyên L, tìm và in ra giá trị lớn nhất trong L
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))
# Tìm và in ra giá trị lớn nhất
max_value = max(L)
print("Giá trị lớn nhất trong list là:", max_value)