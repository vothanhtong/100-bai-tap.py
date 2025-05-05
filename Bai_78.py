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

def in_bang_cuu_chuong(n):
    """
    In bảng cửu chương của một số nguyên.
    Args:
        n (int): Số nguyên cần in bảng cửu chương.
    """
    print(f"Bảng cửu chương của {n}:")
    for i in range(1, 11):  # Từ 1 đến 10
        print(f"{n} x {i} = {n * i}")
    print("-" * 20)


def so_sanh_va_in_bang_cuu_chuong(a, b):
    """
    So sánh hai số nguyên và in bảng cửu chương của số lớn hơn.
    Nếu hai số bằng nhau, in bảng cửu chương của cả hai số.
    Args:
        a (int): Số nguyên thứ nhất.
        b (int): Số nguyên thứ hai.
    """
    if a > b:
        print(f"{a} lớn hơn {b}.")
        in_bang_cuu_chuong(a)
    elif b > a:
        print(f"{b} lớn hơn {a}.")
        in_bang_cuu_chuong(b)
    else:
        print(f"Hai số {a} và {b} bằng nhau.")
        in_bang_cuu_chuong(a)


def main():
    try:
        # Nhập hai số nguyên từ người dùng
        num1 = int(input("Nhập số nguyên thứ nhất: "))
        num2 = int(input("Nhập số nguyên thứ hai: "))

        # Gọi hàm để so sánh và in bảng cửu chương
        so_sanh_va_in_bang_cuu_chuong(num1, num2)
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()