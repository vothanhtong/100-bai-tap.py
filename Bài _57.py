# BÀI 57: Nhập vào một list L, hãy tìm và in ra giá trị âm lớn nhất trong L, nếu L không có giá trị âm thì ta in 0
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Lọc các giá trị âm trong list
negative_numbers = [num for num in L if num < 0]

# Tìm giá trị âm lớn nhất nếu có, nếu không thì in ra 0
if negative_numbers:
    max_negative = max(negative_numbers)
    print("Giá trị âm lớn nhất là:", max_negative)
else:
    print(0)