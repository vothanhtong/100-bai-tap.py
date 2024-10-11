# BÀI 59:Nhập vào một list số nguyên L, tính giá trị trung bình của list L
# # Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Tính giá trị trung bình của list
if len(L) > 0:
    avg = sum(L) / len(L)
    print("Giá trị trung bình của list là:", avg)
else:
    print("List rỗng, không thể tính giá trị trung bình.")