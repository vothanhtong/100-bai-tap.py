# BÀI 45: Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên cách nhau một dấu phẩy, hãy tính tổng 3 số nguyên đó
chuoi = input("nhập vào một chuỗi có ba số nguyên: ")
a = chuoi.find(",")
b = chuoi.rfind(",")
so1 = int(chuoi[:a])
so2 = int(chuoi[a+1:b])
so3 = int(chuoi[b+1])
print(so1 + so2 + so3)
def tinh_tong_tu_chuoi(chuoi):
    """
    Tính tổng các số nguyên trong chuỗi, mỗi số cách nhau bằng dấu phẩy.
    Args:
        chuoi (str): Chuỗi chứa các số nguyên cách nhau bằng dấu phẩy.
    Returns:
        int: Tổng các số nguyên.
    """
    try:
        # Tách chuỗi thành danh sách các số nguyên
        so_nguyen = list(map(int, chuoi.split(",")))
        # Tính tổng
        return sum(so_nguyen)
    except ValueError:
        raise ValueError("Chuỗi không hợp lệ. Vui lòng nhập các số nguyên cách nhau bằng dấu phẩy.")

def main():
    # Nhập chuỗi từ người dùng
    chuoi = input("Nhập vào một chuỗi có các số nguyên cách nhau bằng dấu phẩy: ")
    try:
        # Tính tổng và in kết quả
        tong = tinh_tong_tu_chuoi(chuoi)
        print(f"Tổng các số nguyên trong chuỗi là: {tong}")
    except ValueError as e:
        print(f"Lỗi: {e}")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()