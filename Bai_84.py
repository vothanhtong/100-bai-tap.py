# # Bài 84 :Viết hàm có tham số đầu vào là một list L có các phần tử là chuỗi. Hãy tạo ra một dictionary D mã hóa, với mỗi một phần tử trong L được mã hóa thành một con số (theo thứ tự từ 0 tăng dần lên 1 đơn vị). Sau đó trả về list đã được mã hóa
# # Ví dụ:
# # Cho
# # L = ["đen","vàng","xanh","vàng","xanh","đỏ","hồng"]
# # Xây dựng dictionary mã hóa:
# # D = {'đen':0,'vàng':1,'xanh':2,'đỏ':3,'hồng':4}
# # Trả về List mã hóa:
# # L_mahoa = [0, 1, 2, 1, 2, 3, 4]
# def ma_hoa_list(L):
#     D = {}  # Tạo dictionary mã hóa
#     L_mahoa = []  # Danh sách mã hóa

#     # Bước 1: Tạo dictionary mã hóa
#     for item in L:
#         if item not in D:
#             D[item] = len(D)  # Gán mã cho phần tử mới
#         L_mahoa.append(D[item])  # Thêm giá trị mã hóa vào danh sách kết quả

#     return L_mahoa, D  # Trả về danh sách mã hóa và dictionary

# # Ví dụ sử dụng
# L = ["đen", "vàng", "xanh", "vàng", "xanh", "đỏ", "hồng"]
# L_mahoa, D = ma_hoa_list(L)
# print("List mã hóa:", L_mahoa)  # Kết quả sẽ là [0, 1, 2, 1, 2, 3, 4]
# print("Dictionary mã hóa:", D)   # Kết quả sẽ là {'đen': 0, 'vàng': 1, 'xanh': 2, 'đỏ': 3, 'hồng': 4}
