# BÀI 60: Nhập vào một list số nguyên L, hãy kiểm tra xem L có được sắp xếp từ bé đến lớn hay không, nếu có thì in True, không có thì in False
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Kiểm tra xem list có được sắp xếp từ bé đến lớn hay không
if L == sorted(L):
    print(True)
else:
    print(False)