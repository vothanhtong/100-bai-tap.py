# # BÀI 79 :Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tính và trả về giá trị trung bình của a phần tử đầu tiên trong L
# def average_of_first_a_elements(L, a):
#     # Kiểm tra nếu a lớn hơn số phần tử trong L
#     if a > len(L):
#         return None  # Trả về None nếu a lớn hơn số phần tử trong L
    
#     # Lấy a phần tử đầu tiên
#     first_a_elements = L[:a]
    
#     # Tính trung bình
#     average = sum(first_a_elements) / a
#     return average
