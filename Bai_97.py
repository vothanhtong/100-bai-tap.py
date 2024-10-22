# Bài 97: Cho N (N ≤ 100) điểm trên hệ trục tọa độ Oxy, hãy đếm xem có bao nhiêu tam giác cân được tạo thành từ các điểm đó.
# File tgcan.inp:
# - Dòng đầu tiên trong file chứa số N
# - N dòng tiếp theo chứa các cặp tọa độ các điểm (mỗi dòng một cặp, mỗi số cách nhau một khoảng trắng)
# Ghi vào file tgcan.out số lượng tam giác cân tạo được
# VD:
# tgcan.inp	tgcan.out
# 4
# 0 0
# 1 0
# 2 0
# 1 1
# 3
# def khoang_cach_binh_phuong(p1, p2):
#     # Tính bình phương khoảng cách giữa hai điểm p1 và p2
#     return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

# def dem_tam_giac_can(input_file, output_file):
#     with open(input_file, 'r') as inp:
#         N = int(inp.readline().strip())  # Đọc số điểm N
#         points = [tuple(map(int, inp.readline().strip().split())) for _ in range(N)]  # Đọc tọa độ các điểm

#     count = 0  # Đếm số lượng tam giác cân

#     # Kiểm tra tất cả các bộ ba điểm để xác định tam giác cân
#     for i in range(N):
#         for j in range(i + 1, N):
#             for k in range(j + 1, N):
#                 # Tính bình phương khoảng cách giữa các cặp điểm
#                 d1 = khoang_cach_binh_phuong(points[i], points[j])
#                 d2 = khoang_cach_binh_phuong(points[j], points[k])
#                 d3 = khoang_cach_binh_phuong(points[i], points[k])
                
#                 # Kiểm tra xem có cặp cạnh nào bằng nhau
#                 if d1 == d2 or d1 == d3 or d2 == d3:
#                     count += 1  # Nếu có, tăng số lượng tam giác cân

#     # Ghi kết quả vào file
#     with open(output_file, 'w') as out:
#         out.write(str(count) + '\n')

# Sử dụng hàm với file cụ thể
# dem_tam_giac_can('tgcan.inp', 'tgcan.out')
