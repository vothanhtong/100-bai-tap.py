# Bài 81:Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a.
#  Hãy tìm và trả về giá trị lớn thứ a trong list L (nếu a = 1 thì tìm giá trị lớn nhất, a = 2 thì tìm giá trị lớn nhì, a = 3 thì tìm giá trị lớn ba,...)
# C1 
# def gia_tri_lon_thu_a(L, a):
#     # Bước 1: Sắp xếp danh sách theo thứ tự giảm dần
#     L_unique = list(set(L))  # Loại bỏ các giá trị trùng lặp
#     L_unique.sort(reverse=True)  # Sắp xếp giảm dần

#     # Bước 2: Kiểm tra xem giá trị thứ a có tồn tại không
#     if a <= len(L_unique):
#         return L_unique[a - 1]  # Trả về giá trị lớn thứ a (a-1 là chỉ số)
#     else:
#         return None  # Trả về None nếu a lớn hơn số phần tử độc nhất trong L

# # Ví dụ sử dụng
# L = [3, 1, 4, 4, 2, 5]
# a = 2
# result = gia_tri_lon_thu_a(L, a)
# print(result)  # Kết quả sẽ là 4
# # c2:
# def gia_tri_lon_thu_a(L, a):
#     # Loại bỏ các số trùng lặp bằng cách chuyển sang tập hợp
#     unique_values = list(set(L))
    
#     # Sắp xếp danh sách theo thứ tự giảm dần
#     unique_values.sort(reverse=True)
    
#     # Kiểm tra xem a có nằm trong phạm vi số phần tử không
#     if a <= len(unique_values):
#         return unique_values[a - 1]  # Trả về giá trị lớn thứ a
#     else:
#         return None  # Trả về None nếu không có giá trị lớn thứ a

# # Ví dụ sử dụng
# L = [3, 1, 4, 4, 5, 5, 2]
# a = 2
# print(gia_tri_lon_thu_a(L, a))  # Kết quả sẽ là 4