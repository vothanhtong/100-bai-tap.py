# BÀI 68 : Nhập vào một list số nguyên L, hãy biến đổi L bằng cách thay đổi vị trí giữa giá trị nhỏ nhất và lớn nhất
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Kiểm tra list không rỗng
if not L:
    print("List rỗng!")
else:
    # Tìm chỉ số của giá trị nhỏ nhất và lớn nhất
    min_index = L.index(min(L))
    max_index = L.index(max(L))

    # Hoán đổi giá trị nhỏ nhất và lớn nhất
    L[min_index], L[max_index] = L[max_index], L[min_index]

    # In ra list đã biến đổi
    print("List sau khi hoán đổi:", L)