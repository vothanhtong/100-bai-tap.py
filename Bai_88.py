# # Bài 88: Viết hàm cho giá trị đầu vào là list số nguyên dương L và số nguyên dương k. 
# # Tìm và trả về đoạn list dài nhất trong L có giá trị trung bình là k
# def tim_doan_list_trung_binh_k(L, k):
#     n = len(L)  # Số phần tử trong danh sách L
#     max_len = 0  # Độ dài lớn nhất của đoạn tìm thấy
#     longest_sublist = []  # Đoạn dài nhất tìm thấy

#     # Duyệt qua tất cả các đoạn con trong L
#     for i in range(n):
#         for j in range(i, n):
#             sublist = L[i:j+1]  # Lấy đoạn từ i đến j
#             avg = sum(sublist) / len(sublist)  # Tính trung bình của đoạn con

#             # Kiểm tra xem giá trị trung bình có bằng k không
#             if avg == k:
#                 if len(sublist) > max_len:  # Nếu độ dài đoạn con này lớn hơn đoạn dài nhất trước đó
#                     max_len = len(sublist)
#                     longest_sublist = sublist

#     return longest_sublist
# # Ví dụ sử dụng
# L = [1, 2, 3, 4, 5, 6, 7]
# k = 4
# longest_sublist = tim_doan_list_trung_binh_k(L, k)
# print(longest_sublist)  # Kết quả sẽ là [3, 4, 5]

def tim_doan_list_trung_binh_k(L, k):
    """
    Tìm đoạn list dài nhất có giá trị trung bình bằng k.

    Args:
        L (list): Danh sách các số nguyên dương.
        k (int): Giá trị trung bình cần tìm.

    Returns:
        list: Đoạn list dài nhất có giá trị trung bình bằng k.
    """
    if not all(isinstance(x, int) and x > 0 for x in L) or not isinstance(k, int) or k <= 0:
        raise ValueError("Danh sách L phải chứa số nguyên dương và k phải là số nguyên dương.")

    n = len(L)
    max_len, longest_sublist = 0, []

    for i in range(n):
        total = 0  # Tổng các phần tử trong đoạn con
        for j in range(i, n):
            total += L[j]
            avg = total / (j - i + 1)
            if avg == k and (j - i + 1) > max_len:
                max_len = j - i + 1
                longest_sublist = L[i:j+1]

    return longest_sublist

# Ví dụ sử dụng
L = [1, 2, 3, 4, 5, 6, 7]
k = 4
longest_sublist = tim_doan_list_trung_binh_k(L, k)
print(longest_sublist)  # Kết quả sẽ là [3, 4, 5]