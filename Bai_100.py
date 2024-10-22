# Bài 100: Cho trước số tự nhiên N. Hãy viết chương trình cho biết N có thể biểu diễn thành tổng của hai hoặc nhiều số tự nhiên liên tiếp hay không? Nếu có, thì bao nhiêu cách và hãy liệt kê tất cả các cách có thể có. Nếu không, thì thông báo bằng số 0.
# File bieudienso.inp:
# - Chứa N
# File bieudienso.out:
# - Chứa các trường hợp có thể tách được, mỗi số cách nhau một dấu cộng, mỗi dòng một trường hợp
# VD:

# bieudienso.inp	bieudienso.out
# 9	2
# 4+5
# 2+3+4
# def bieudienso(input_file, output_file):
#     with open(input_file, 'r') as inp:
#         N = int(inp.readline().strip())
    
#     results = []
#     count = 0
    
#     # Duyệt từ k = 2 đến một giá trị k hợp lệ
#     for k in range(2, N):
#         # Tính tổng k(k-1)/2
#         sum_k_minus_1 = k * (k - 1) // 2
        
#         if sum_k_minus_1 >= N:
#             break
        
#         if (N - sum_k_minus_1) % k == 0:
#             a = (N - sum_k_minus_1) // k
#             if a > 0:  # a phải là số tự nhiên
#                 count += 1
#                 sequence = '+'.join(str(a + i) for i in range(k))
#                 results.append(sequence)

#     # Ghi kết quả vào file
#     with open(output_file, 'w') as out:
#         if count == 0:
#             out.write('0\n')
#         else:
#             out.write(f'{count}\n')
#             out.write('\n'.join(results) + '\n')

# # Sử dụng hàm với file cụ thể
# bieudienso('bieudienso.inp', 'bieudienso.out')
