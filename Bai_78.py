# # BÀI 78 :Viết hàm đưa vào 1 list có các phần tử là chuỗi, tìm và trả về chuỗi ngắn nhất trong list
# def find_shortest_string(lst):
#     if len(lst) == 0:
#         return None  # Trả về None nếu danh sách rỗng

#     shortest_string = lst[0]  # Bắt đầu với chuỗi đầu tiên

#     # Duyệt qua danh sách để tìm chuỗi ngắn nhất
#     for string in lst:
#         if len(string) < len(shortest_string):
#             shortest_string = string  # Cập nhật chuỗi ngắn nhất

#     return shortest_string