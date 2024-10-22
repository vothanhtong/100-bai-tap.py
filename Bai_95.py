# Bài 95:Cho một dãy số 1, 1, 1, 2, 3, 4, 6,... (quy luật a[i] = a[i - 1] + a[i - 3])
# Với a[1] = 1, a[2] = 1, a[3] = 1 (3 số đầu tiên)
# File dayso.inp chứa các số nguyên k (k < 1000), mỗi dòng 1 số
# Hãy tìm a[k] trong dãy số và ghi vào file dayso.out
# VD:
# dayso.inp	
# dayso.out
# 3
# 10
# 50
# 101	1
# 19
# 83316385
# 24382819596721629
# def tinh_day_so(max_k):
#     # Khởi tạo dãy với 3 phần tử đầu là 1
#     a = [0] * (max_k + 1)
#     a[1] = a[2] = a[3] = 1
    
#     # Tính toán các giá trị tiếp theo dựa trên công thức
#     for i in range(4, max_k + 1):
#         a[i] = a[i - 1] + a[i - 3]
    
#     return a

# def xu_ly_file(input_file, output_file):
#     # Đọc các số k từ file đầu vào
#     with open(input_file, 'r') as inp:
#         k_list = [int(line.strip()) for line in inp.readlines()]
    
#     # Tìm giá trị lớn nhất của k trong file để tính đến giá trị đó
#     max_k = max(k_list)
    
#     # Tính dãy số đến giá trị max_k
#     day_so = tinh_day_so(max_k)
    
#     # Ghi kết quả tương ứng của từng k vào file đầu ra
#     with open(output_file, 'w') as out:
#         for k in k_list:
#             out.write(str(day_so[k]) + '\n')

# # Sử dụng hàm với file cụ thể
# xu_ly_file('dayso.inp', 'dayso.out')