# # BÀI 55: Nhập vào một list số nguyên L, hãy kiểm tra xem tất cả các phần tử trong mảng có bằng nhau hay không, nếu có thì in True, không có thì in False
# Nhập vào list số nguyên
# Nhập danh sách số nguyên
L = list(map(int, input("Nhập các phần tử của list cách nhau bằng dấu cách: ").split()))
# Kiểm tra nếu tất cả các phần tử trong list đều bằng nhau
if all(x == L[0] for x in L):
    print(True)
else:
    print(False)
