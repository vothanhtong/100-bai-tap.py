# # BÀI TẬP XỬ LÝ DICTIONARY

# # Bài 82: Viết hàm đưa vào 1 dictionary có các phần tử có giá trị là số nguyên, tìm và trả về key có giá trị lớn nhất
# def key_max_value(d):
#     if not d:
#         return None  # Trả về None nếu dictionary rỗng

#     # Tìm key có giá trị lớn nhất
#     max_key = max(d, key=d.get)  # Sử dụng hàm max với tham số key để tìm key tương ứng
#     return max_key

# # Ví dụ sử dụng
# d = {'a': 10, 'b': 20, 'c': 15}
# result = key_max_value(d)
# print(result)  # Kết quả sẽ là 'b'