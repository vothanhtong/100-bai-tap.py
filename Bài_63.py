# BÀI 63: Nhập vào một list số nguyên L, Hãy tìm và in ra một vị trí trong L thỏa hai điều kiện: có hai giá trị lân cận và giá trị tại vị trí đó bằng tích hai giá trị lân cận.
# Nếu L không tồn tại giá trị như vậy thì in ra - 1
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Biến để lưu vị trí tìm thấy
position = -1

# Duyệt qua list từ phần tử thứ 1 đến phần tử thứ len(L) - 2
for i in range(1, len(L) - 1):
    if L[i] == L[i - 1] * L[i + 1]:
        position = i
        break  # Ngắt vòng lặp khi tìm thấy

# In ra vị trí thỏa mãn điều kiện hoặc -1 nếu không tìm thấy
print(position)