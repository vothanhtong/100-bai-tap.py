# BÀI 70 : Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy kiểm tra các phần tử trong L có phải là chuỗi và số xen kẽ nhau không, nếu có thì ta tiến hành tạo một list K mới có các phần tử như sau:
# K[i/2] = L[i]*L[i+1] (với i chẵn)
# Nhập vào list có các phần tử bao gồm chuỗi và số nguyên
L = eval(input("Nhập list gồm các phần tử chuỗi và số nguyên (vd: [1, 'abc', 2, 'de', 3]): "))

# Biến để lưu list mới K
K = []

# Kiểm tra tính xen kẽ
is_alternating = True
for i in range(len(L)):
    if (i % 2 == 0 and not isinstance(L[i], str)) or (i % 2 == 1 and not isinstance(L[i], int)):
        is_alternating = False
        break

# Nếu là xen kẽ, tạo list K
if is_alternating:
    for i in range(0, len(L) - 1, 2):  # Duyệt từ 0 đến len(L) - 1 với bước 2
        # Kiểm tra nếu phần tử i là chuỗi và phần tử i+1 là số nguyên
        if isinstance(L[i], str) and isinstance(L[i + 1], int):
            K.append(L[i] * L[i + 1])  # Tạo phần tử K[i/2] = L[i] * L[i+1]

    # In ra kết quả
    print("List K mới là:", K)
else:
    print("Các phần tử trong list không phải là chuỗi và số xen kẽ nhau.")