# # Bài 87:Viết hàm cho giá trị đầu vào là list số nguyên dương L và số nguyên dương k.
# #  Hãy tạo và trả về một list L_kq có các phần tử là giá trị của phần tử xuất hiện nhiều hơn k lần trong list L theo thứ tự tăng dần
# def tim_phan_tu_xuat_hien_hon_k(L, k):
#     # Bước 1: Tạo dictionary đếm số lần xuất hiện của từng phần tử
#     dem = {}
#     for num in L:
#         if num in dem:
#             dem[num] += 1
#         else:
#             dem[num] = 1

#     # Bước 2: Tìm các phần tử xuất hiện nhiều hơn k lần
#     L_kq = [num for num, count in dem.items() if count > k]

#     # Bước 3: Sắp xếp danh sách kết quả theo thứ tự tăng dần
#     L_kq.sort()

#     return L_kq
# # Ví dụ sử dụng
# L = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# k = 2
# L_kq = tim_phan_tu_xuat_hien_hon_k(L, k)
# print(L_kq)  # Kết quả sẽ là [3, 4]s