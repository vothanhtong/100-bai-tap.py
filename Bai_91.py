# Đề bài:
# Một khách sạn có N phòng đôi được đánh số từ 1 đến N và có M đoàn khách. Với mỗi đoàn khách:

# Mỗi cặp khách của đoàn sẽ được xếp vào một phòng trống theo thứ tự phòng tăng dần.
# Nếu đoàn khách có số người lẻ, người khách cuối cùng sẽ được xếp vào một phòng trống tiếp theo.
# Nếu đã hết phòng trống, khách sẽ được xếp vào những phòng đã có 1 khách theo thứ tự phòng tăng dần.
# Hãy viết chương trình để in ra số lượng khách trong mỗi phòng sau khi xếp.

# Input:

# N: Số lượng phòng.
# doankhach: Danh sách số lượng khách của từng đoàn.
# Output:

# Danh sách số lượng khách trong từng phòng sau khi xếp.
# Ví dụ:

# Input: N = 7, doankhach = [3, 7, 3]
# Output: [2, 2, 2, 2, 2, 1, 2]
# Input: N = 5, doankhach = [2, 3, 2]
# Output: [2, 2, 1, 2, 0]
# Code tối ưu:
# Giải thích tối ưu:
# Khởi tạo danh sách phòng:

# phong = [0] * N: Mỗi phần tử trong danh sách đại diện cho số lượng khách trong một phòng.
# Xếp khách vào phòng:

# Sử dụng min(so_khach, 2 - phong[index]) để tính số khách có thể xếp vào phòng hiện tại (tối đa 2 khách mỗi phòng).
# Cập nhật số khách còn lại (so_khach -= xep_vao_phong) và số khách trong phòng (phong[index] += xep_vao_phong).
# Chuyển sang phòng tiếp theo:

# index = (index + 1) % N: Tự động quay lại phòng đầu tiên nếu đã duyệt hết các phòng.
# Trả về kết quả:

# Hàm trả về danh sách phong chứa số lượng khách trong từng phòng.
# Kết quả chạy:
# Với N = 7, doankhach = [3, 7, 3]:
# Output: [2, 2, 2, 2, 2, 1, 2]
# Với N = 5, doankhach = [2, 3, 2]:
# Output: [2, 2, 1, 2, 0]
# Ưu điểm của phiên bản tối ưu:
# Ngắn gọn và dễ hiểu: Code được viết ngắn gọn, không có logic thừa.
# Hiệu quả: Sử dụng vòng lặp đơn giản để duyệt qua các phòng và xếp khách.
# Tái sử dụng: Hàm trả về danh sách kết quả, dễ dàng sử dụng trong các bài toán khác hoặc kiểm tra kết quả.

def xep_khach_san(N, doankhach):
    """
    Hàm xếp khách vào phòng đôi của khách sạn.
    :param N: Số lượng phòng
    :param doankhach: Danh sách số lượng khách của từng đoàn
    :return: Danh sách số lượng khách trong từng phòng
    """
    phong = [0] * N  # Khởi tạo danh sách số lượng khách trong mỗi phòng
    index = 0  # Vị trí phòng hiện tại

    for so_khach in doankhach:
        while so_khach > 0:
            # Xếp khách vào phòng hiện tại, tối đa 2 khách mỗi phòng
            xep_vao_phong = min(so_khach, 2 - phong[index])
            phong[index] += xep_vao_phong
            so_khach -= xep_vao_phong

            # Chuyển sang phòng tiếp theo
            index = (index + 1) % N

    return phong

# Ví dụ sử dụng:
print(xep_khach_san(7, [3, 7, 3]))  # Output: [2, 2, 2, 2, 2, 1, 2]
print(xep_khach_san(5, [2, 3, 2]))  # Output: [2, 2, 1, 2, 0]