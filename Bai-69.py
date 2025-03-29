# BÀI 69 :Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy tìm và in ra chuỗi có độ dài lớn nhất và số nguyên có giá trị nhỏ nhất
# Nhập vào list có các phần tử bao gồm chuỗi và số nguyên
L = eval(input("Nhập list gồm các phần tử chuỗi và số nguyên (vd: [1, 'abc', 2, 'de', -1]): "))

# Biến để lưu chuỗi có độ dài lớn nhất và số nguyên nhỏ nhất
longest_string = ""
smallest_integer = float('inf')  # Khởi tạo là dương vô cực

# Duyệt qua từng phần tử trong list
for item in L:
    # Kiểm tra nếu phần tử là chuỗi
    if isinstance(item, str):
        if len(item) > len(longest_string):
            longest_string = item  # Cập nhật chuỗi có độ dài lớn nhất
    # Kiểm tra nếu phần tử là số nguyên
    elif isinstance(item, int):
        if item < smallest_integer:
            smallest_integer = item  # Cập nhật số nguyên nhỏ nhất

# In ra kết quả
print("Chuỗi có độ dài lớn nhất:", longest_string)
print("Số nguyên có giá trị nhỏ nhất:", smallest_integer if smallest_integer != float('inf') else "Không có số nguyên")

# BÀI 70: Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy tìm và in ra chuỗi có độ dài nhỏ nhất và số nguyên có giá trị lớn nhất
# Nhập vào list có các phần tử bao gồm chuỗi và số nguyên
L = eval(input("Nhập list gồm các phần tử chuỗi và số nguyên (vd: [1, 'abc', 2, 'de', -1]): "))

# Biến để lưu chuỗi có độ dài nhỏ nhất và số nguyên lớn nhất
shortest_string = None
largest_integer = float('-inf')  # Khởi tạo là âm vô cực

# Duyệt qua từng phần tử trong list
for item in L:
    # Kiểm tra nếu phần tử là chuỗi
    if isinstance(item, str):
        if shortest_string is None or len(item) < len(shortest_string):
            shortest_string = item  # Cập nhật chuỗi có độ dài nhỏ nhất
    # Kiểm tra nếu phần tử là số nguyên
    elif isinstance(item, int):
        if item > largest_integer:
            largest_integer = item  # Cập nhật số nguyên lớn nhất

# In ra kết quả
print("Chuỗi có độ dài nhỏ nhất:", shortest_string if shortest_string is not None else "Không có chuỗi")
print("Số nguyên có giá trị lớn nhất:", largest_integer if largest_integer != float('-inf') else "Không có số nguyên")