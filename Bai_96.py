# Bài 96: Hai số được coi là bạn của nhau khi tổng các ước số (ngoại trừ chính nó) của số này bằng số kia và ngược lại, cụ thể:
#  tổng ước số của M = N và tổng ước số của N = M thì M và N là bạn
# Trong file soban.inp là số K, hãy liệt kê các cặp số M N (với 1 ≤ M < N ≤ K) và ghi vào file soban.out (mỗi cặp một dòng)
# VD:
# soban.inp	soban.out
# 3000	220 284
# 1184 1210
# 2620 2924
# def tong_uoc_so(n):
#     total = 0
#     # Tính tổng các ước số của n
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:  # Nếu i là ước số của n
#             total += i
#             if i != n // i and i != 1:  # Thêm ước số đối
#                 total += n // i
#     return total

# def tim_cac_cap_ban(input_file, output_file):
#     with open(input_file, 'r') as inp:
#         K = int(inp.read().strip())  # Đọc số K từ file
        
#     cap_ban = []  # Danh sách lưu các cặp bạn
    
#     # Tạo danh sách để lưu tổng các ước số cho từng số
#     tong_uoc = [0] * (K + 1)
    
#     # Tính tổng ước số cho từng số từ 1 đến K
#     for n in range(1, K + 1):
#         tong_uoc[n] = tong_uoc_so(n)
    
#     # Tìm các cặp bạn
#     for M in range(1, K):
#         N = tong_uoc[M]  # Tìm N là tổng ước số của M
#         if M < N <= K and tong_uoc[N] == M:  # Kiểm tra điều kiện bạn
#             cap_ban.append((M, N))
    
#     # Ghi kết quả vào file
#     with open(output_file, 'w') as out:
#         for M, N in cap_ban:
#             out.write(f"{M} {N}\n")

# # Sử dụng hàm với file cụ thể
# tim_cac_cap_ban('soban.inp', 'soban.out')