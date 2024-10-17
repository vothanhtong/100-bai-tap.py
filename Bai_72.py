# BÀI 72: Nhập vào một list L có các phần tử là chuỗi. Hãy tìm ra chuỗi có vị trí ký tự in hoa lớn nhất
# Nhập vào list các chuỗi
L = eval(input("Nhập list gồm các chuỗi (vd: ['Hello World', 'Python Is Fun', 'Learning Python']): "))

# Biến để lưu chuỗi có ký tự in hoa ở vị trí lớn nhất và chỉ số của nó
max_upper_index = -1
result_string = ""

# Duyệt qua từng chuỗi trong list
for string in L:
    # Duyệt qua từng ký tự trong chuỗi
    for index, char in enumerate(string):
        if char.isupper():  # Kiểm tra nếu ký tự là in hoa
            if index > max_upper_index:  # Kiểm tra vị trí ký tự in hoa
                max_upper_index = index
                result_string = string  # Cập nhật chuỗi có vị trí ký tự in hoa lớn nhất

# In ra kết quả
if result_string:
    print("Chuỗi có ký tự in hoa ở vị trí lớn nhất là:", result_string)
else:
    print("Không có ký tự in hoa trong bất kỳ chuỗi nào.")