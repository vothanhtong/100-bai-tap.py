# # Bài 85:Viết hàm có tham số đầu vào là một dictionary, hãy tạo một dictionary mới hoán đổi giá trị và key của dictionary đầu vào, rồi trả về dicionary mới đó.
# #  Nếu sau khi hoán đổi có 2 key trùng nhau (do dictionary đầu vào có 2 giá trị trùng nhau), hàm trả về None
# def hoan_doi_dict(d):
#     d_hoan_doi = {}  # Tạo dictionary mới để hoán đổi

#     for key, value in d.items():
#         # Kiểm tra xem value đã tồn tại trong dictionary mới chưa
#         if value in d_hoan_doi:
#             return None  # Nếu trùng, trả về None
#         d_hoan_doi[value] = key  # Hoán đổi key và value

#     return d_hoan_doi  # Trả về dictionary mới

# # Ví dụ sử dụng
# d = {'a': 1, 'b': 2, 'c': 3}
# d_hoan_doi = hoan_doi_dict(d)
# print(d_hoan_doi)  # Kết quả sẽ là {1: 'a', 2: 'b', 3: 'c'}

# d2 = {'a': 1, 'b': 2, 'c': 1}
# d_hoan_doi2 = hoan_doi_dict(d2)
# print(d_hoan_doi2)  # Kết quả sẽ là None (do có giá trị trùng nhau)