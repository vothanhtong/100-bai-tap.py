# BÀI 71 : Nhập vào một list L có các phần tử là chuỗi (các chuỗi này không có ký tự đặc biệt, dấu câu, ký tự số, chỉ có ký tự chữ cái và khoảng trắng)
# Hãy tìm ra vị trí của chuỗi có nhiều từ nhất
# Nhập vào list các chuỗi
L = eval(input("Nhập list gồm các chuỗi (vd: ['Hello world', 'Python is fun', 'I love programming']): "))

# Biến để lưu vị trí và số từ nhiều nhất
max_words = 0
max_index = -1

# Duyệt qua từng chuỗi trong list
for index, string in enumerate(L):
    word_count = len(string.split())  # Đếm số từ trong chuỗi

    # Kiểm tra nếu số từ trong chuỗi hiện tại lớn hơn số từ lớn nhất đã tìm thấy
    if word_count > max_words:
        max_words = word_count
        max_index = index  # Cập nhật vị trí

# In ra kết quả
if max_index != -1:
    print("Vị trí của chuỗi có nhiều từ nhất là:", max_index)
    print("Chuỗi đó là:", L[max_index])
else:
    print("Không có chuỗi nào trong list.")