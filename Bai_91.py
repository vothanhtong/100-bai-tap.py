# Bài 91:Một khách sạn có N phòng đôi được đánh số từ 1 đến N và M đoàn khách.
# Với mỗi đoàn khách, ta xếp mỗi cặp khách của đoàn vào một phòng trống theo thứ tự phòng tăng dần.
# Nếu đoàn khách có số người lẻ thì người khách cuối cùng được xếp vào một phòng trống tiếp theo.
# Nếu đã hết phòng còn trống thì ta sẽ xếp khách vào những phòng mới chỉ có 1 khách theo thứ tự phòng tăng dần.
# In ra số khách của mỗi phòng sau khi xếp.
# Giả sử không có 2 đoàn khách nào đến cùng một lúc.
# Ví dụ 1:
# N = 7, M = 3
# doankhach = [3,7,3]
# Ta in: 2, 2, 2, 2, 2, 1, 2
# Ví dụ 2:
# N = 5, M = 3
# doankhach = [2,3,2]
# Ta in: 2, 2, 1, 2, 0
# def xep_khach_san(N, M, doankhach):
#     # Bước 1: Khởi tạo danh sách số lượng khách trong mỗi phòng
#     phong = [0] * N  # Ban đầu tất cả các phòng đều trống
    
#     index = 0  # Biến để theo dõi phòng hiện tại

#     # Bước 2: Xếp khách cho từng đoàn
#     for so_khach in doankhach:
#         while so_khach > 0:
#             # Nếu phòng hiện tại còn trống (phong[index] < 2)
#             if phong[index] < 2:
#                 # Số khách xếp vào phòng này (tối đa 2 - phong[index])
#                 xep_vao_phong = min(so_khach, 2 - phong[index])
#                 phong[index] += xep_vao_phong
#                 so_khach -= xep_vao_phong
            
#             # Chuyển sang phòng tiếp theo
#             index += 1
#             if index == N:
#                 index = 0  # Quay lại phòng đầu tiên nếu hết phòng
            
#     # Bước 3: In kết quả
#     print(",".join(map(str, phong)))

# # Ví dụ 1:
# N = 7
# M = 3
# doankhach = [3, 7, 3]
# xep_khach_san(N, M, doankhach)  # Output: 2,2,2,2,2,1,2

# # Ví dụ 2:
# N = 5
# M = 3
# doankhach = [2, 3, 2]
# xep_khach_san(N, M, doankhach)  # Output: 2,2,1,2,0
