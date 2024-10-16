# BÀI 67: Nhập vào một list số nguyên L, hãy đưa các số chẵn trong list về đầu list, số lẻ về cuối list và các phần tử 0 nằm ở giữa
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Khởi tạo các list tạm thời
evens = []  # Danh sách số chẵn
odds = []   # Danh sách số lẻ
zeros = []  # Danh sách số 0

# Duyệt qua từng phần tử trong list
for num in L:
    if num == 0:
        zeros.append(num)  # Thêm số 0 vào danh sách zeros
    elif num % 2 == 0:
        evens.append(num)  # Thêm số chẵn vào danh sách evens
    else:
        odds.append(num)    # Thêm số lẻ vào danh sách odds

# Kết hợp các list lại với nhau
result = evens + zeros + odds

# In ra kết quả
print("List sau khi sắp xếp là:", result)