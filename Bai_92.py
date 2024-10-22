# BÀI TẬP XỬ LÝ ĐỌC GHI FILE
# Bài 92:File 2to10.inp là file chứa các số nhị phân (mỗi dòng 1 số), hãy chuyển các số nhị phân đó sang số thập phân rồi lưu lại vào file 2to10.out (mỗi dòng 1 số)
# VD
# 2to10.inp
# 2to10.out
# 0011
# 111110000011111
# 1001010100000010111110001111111111	3
# 31775
# 9999999999
# def binary_to_decimal(input_file, output_file):
#     with open(input_file, 'r') as inp, open(output_file, 'w') as out:
#         # Đọc từng dòng trong file đầu vào
#         for line in inp:
#             binary_str = line.strip()  # Loại bỏ các ký tự trắng (nếu có)
            
#             try:
#                 # Chuyển từ nhị phân sang thập phân
#                 decimal_number = int(binary_str, 2)
#                 # Ghi kết quả vào file đầu ra
#                 out.write(str(decimal_number) + '\n')
#             except ValueError:
#                 # Nếu không phải là số nhị phân hợp lệ thì ghi "INVALID"
#                 out.write("INVALID\n")

# # Sử dụng hàm với file cụ thể
# binary_to_decimal('2to10.inp', '2to10.out')