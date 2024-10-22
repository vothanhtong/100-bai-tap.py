# Bài 93:Hãy phân tích một số tự nhiên thành các thừa số nguyên tố
# File thuaso.inp:
# - Chứa các số tự nhiên lớn hơn 1(mỗi số cách nhau một dòng)
# File thuaso.out:
# - Kết quả phân tích từng số trong file thuaso.inp, 
# mỗi một dòng tương ứng với kết quả tách được được từ trong file thuaso.inp, các thừa số cách nhau bằng một khoảng trắng
# VD:
# thuaso.inp	thuaso.out
# 2
# 8
# 10
# 15
# 100
# 101
# 10250	2
# 2 2 2
# 2 5
# 3 5
# 2 2 5 5
# 101
# 2 5 5 5 41
# def phan_tich_thua_so(n):
#     i = 2
#     thua_so = []
#     # Phân tích số n thành thừa số nguyên tố
#     while i * i <= n:  # Kiểm tra các thừa số từ 2 đến sqrt(n)
#         while n % i == 0:  # Nếu n chia hết cho i
#             thua_so.append(i)
#             n //= i  # Chia n cho i
#         i += 1
#     if n > 1:  # Số còn lại là thừa số nguyên tố cuối cùng
#         thua_so.append(n)
#     return thua_so

# def xu_ly_file(input_file, output_file):
#     with open(input_file, 'r') as inp, open(output_file, 'w') as out:
#         # Đọc từng dòng trong file đầu vào
#         for line in inp:
#             number = int(line.strip())  # Lấy số tự nhiên từ file
#             thua_so = phan_tich_thua_so(number)  # Phân tích thành thừa số
#             # Ghi kết quả vào file, các thừa số cách nhau bằng khoảng trắng
#             out.write(" ".join(map(str, thua_so)) + "\n")

# # Sử dụng hàm với file thuaso.inp và thuaso.out
# xu_ly_file('thuaso.inp', 'thuaso.out')