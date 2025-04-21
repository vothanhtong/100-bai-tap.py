# BÀI  43: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu từ (quy định là chuỗi không có ký tự đặc biệt,
# không số, không có dấu câu, chỉ có ký tự chữ và khoảng trắng)
a=input("nhập vào một chuỗi : ")
chuoi= a.count(" ")
print(chuoi+1)
def dem_so_tu(chuoi):
    """
    Đếm số từ trong chuỗi (chỉ chứa ký tự chữ và khoảng trắng).
    Args:
        chuoi (str): Chuỗi cần đếm từ.
    Returns:
        int: Số từ trong chuỗi.
    """
    # Loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi
    chuoi = chuoi.strip()
    
    # Kiểm tra chuỗi rỗng
    if not chuoi:
        return 0

    # Tách từ bằng split() và trả về độ dài danh sách từ
    return len(chuoi.split())

def main():
    # Nhập chuỗi từ người dùng
    chuoi = input("Nhập vào một chuỗi: ")

    # Đếm số từ và in kết quả
    so_tu = dem_so_tu(chuoi)
    print(f"Số từ trong chuỗi là: {so_tu}")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()

    return len(chuoi.replace(" ", ""))
    