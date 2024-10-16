# BÀI 64:Người ta định nghĩa một list số nguyên là list chẵn lẻ, nếu như tổng 2 phần tử bất kỳ bên trong list đều là số lẻ
# Nhập vào một list số nguyên L và kiểm tra xem L có phải là list chẵn lẻ hay không
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Kiểm tra xem list có phải là list chẵn lẻ hay không
def is_odd_list(seq):
    for num in seq:
        if num % 2 == 0:  # Kiểm tra xem số có phải là số chẵn không
            return False  # Nếu có số chẵn thì không phải list chẵn lẻ
    return True  # Nếu tất cả số đều lẻ

# Gọi hàm kiểm tra và in ra kết quả
if is_odd_list(L):
    print("List là list chẵn lẻ.")
else:
    print("List không phải là list chẵn lẻ.")