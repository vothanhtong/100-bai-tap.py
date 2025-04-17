# Bài 95:Cho một dãy số 1, 1, 1, 2, 3, 4, 6,... (quy luật a[i] = a[i - 1] + a[i - 3])
# Với a[1] = 1, a[2] = 1, a[3] = 1 (3 số đầu tiên)
# File dayso.inp chứa các số nguyên k (k < 1000), mỗi dòng 1 số
# Hãy tìm a[k] trong dãy số và ghi vào file dayso.out
# VD:
# dayso.inp	
# dayso.out
# 3
# 10
# 50
# 101	1
# 19
# 83316385
# 24382819596721629
# def tinh_day_so(max_k):
#     # Khởi tạo dãy với 3 phần tử đầu là 1
#     a = [0] * (max_k + 1)
#     a[1] = a[2] = a[3] = 1
    
#     # Tính toán các giá trị tiếp theo dựa trên công thức
#     for i in range(4, max_k + 1):
#         a[i] = a[i - 1] + a[i - 3]
    
#     return a

# def xu_ly_file(input_file, output_file):
#     # Đọc các số k từ file đầu vào
#     with open(input_file, 'r') as inp:
#         k_list = [int(line.strip()) for line in inp.readlines()]
    
#     # Tìm giá trị lớn nhất của k trong file để tính đến giá trị đó
#     max_k = max(k_list)
    
#     # Tính dãy số đến giá trị max_k
#     day_so = tinh_day_so(max_k)
    
#     # Ghi kết quả tương ứng của từng k vào file đầu ra
#     with open(output_file, 'w') as out:
#         for k in k_list:
#             out.write(str(day_so[k]) + '\n')

# # Sử dụng hàm với file cụ thể
# xu_ly_file('dayso.inp', 'dayso.out')
# Bài 95: Cho một dãy số 1, 1, 1, 2, 3, 4, 6,... (quy luật a[i] = a[i - 1] + a[i - 3])
# Với a[1] = 1, a[2] = 1, a[3] = 1 (3 số đầu tiên)
# File dayso.inp chứa các số nguyên k (k < 1000), mỗi dòng 1 số
# Hãy tìm a[k] trong dãy số và ghi vào file dayso.out
# Bài 95: Cho một dãy số 1, 1, 1, 2, 3, 4, 6,... (quy luật a[i] = a[i - 1] + a[i - 3])
# Với a[1] = 1, a[2] = 1, a[3] = 1 (3 số đầu tiên)  
def tinh_day_so(max_k):
    """
    Tính dãy số theo quy luật a[i] = a[i-1] + a[i-3].
    Args:
        max_k (int): Giá trị lớn nhất cần tính trong dãy.
    Returns:
        list: Dãy số từ a[1] đến a[max_k].
    """
    # Khởi tạo dãy với 3 phần tử đầu là 1
    a = [0] * (max_k + 1)
    a[1] = a[2] = a[3] = 1

    # Tính toán các giá trị tiếp theo dựa trên công thức
    for i in range(4, max_k + 1):
        a[i] = a[i - 1] + a[i - 3]

    return a


def xu_ly_file(input_file, output_file):
    """
    Đọc file đầu vào, tính toán dãy số và ghi kết quả vào file đầu ra.
    Args:
        input_file (str): Đường dẫn đến file đầu vào.
        output_file (str): Đường dẫn đến file đầu ra.
    """
    try:
        # Đọc các số k từ file đầu vào
        with open(input_file, 'r') as inp:
            k_list = [int(line.strip()) for line in inp.readlines()]

        # Kiểm tra giá trị hợp lệ
        if not all(1 <= k < 1000 for k in k_list):
            raise ValueError("Các giá trị trong file phải là số nguyên dương nhỏ hơn 1000.")

        # Tìm giá trị lớn nhất của k trong file để tính đến giá trị đó
        max_k = max(k_list)

        # Tính dãy số đến giá trị max_k
        day_so = tinh_day_so(max_k)

        # Ghi kết quả tương ứng của từng k vào file đầu ra
        with open(output_file, 'w') as out:
            for k in k_list:
                out.write(str(day_so[k]) + '\n')

        print(f"Đã xử lý xong file. Kết quả được ghi vào '{output_file}'.")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{input_file}'.")
    except ValueError as e:
        print(f"Lỗi: {e}")


# Sử dụng hàm với file cụ thể
if __name__ == "__main__":
    input_file = 'dayso.inp'
    output_file = 'dayso.out'
    xu_ly_file(input_file, output_file)