# BÀI 21:Ngày vào ngày, tháng. Hãy tính và in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày 
# (giả sư năm đó không phải là năm nhuận)
a=int(input("nhập vào ngày mà bạn muốn tìm: "))
b=int(input("nhập vào tháng bạn muốn tìm:  "))
if b<=8:
    sothang30ngay=(b-1)//2
    sothang31ngay=b//2
else:
    sothang30ngay=b//2-1
    sothang31ngay=(b+1)//2
songay=a+sothang30ngay*30 +sothang31ngay*31
if b>2:
    songay-=2
print (songay)

def tinh_so_ngay_trong_nam(ngay, thang):
    """
    Tính số ngày từ đầu năm đến ngày nhập vào (không tính năm nhuận).
    Args:
        ngay (int): Ngày nhập vào.
        thang (int): Tháng nhập vào.
    Returns:
        int: Số ngày từ đầu năm đến ngày nhập vào.
    """
    # Số ngày trong từng tháng (không phải năm nhuận)
    so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Kiểm tra tính hợp lệ của ngày và tháng
    if thang < 1 or thang > 12:
        raise ValueError("Tháng không hợp lệ. Vui lòng nhập từ 1 đến 12.")
    if ngay < 1 or ngay > so_ngay_trong_thang[thang - 1]:
        raise ValueError(f"Ngày không hợp lệ. Tháng {thang} chỉ có {so_ngay_trong_thang[thang - 1]} ngày.")

    # Tính tổng số ngày
    return sum(so_ngay_trong_thang[:thang - 1]) + ngay


def tinh_so_ngay_con_lai(ngay, thang):
    """
    Tính số ngày còn lại trong năm từ ngày nhập vào (không tính năm nhuận).
    Args:
        ngay (int): Ngày nhập vào.
        thang (int): Tháng nhập vào.
    Returns:
        int: Số ngày còn lại trong năm.
    """
    tong_so_ngay_trong_nam = 365  # Không tính năm nhuận
    so_ngay_da_qua = tinh_so_ngay_trong_nam(ngay, thang)
    return tong_so_ngay_trong_nam - so_ngay_da_qua


def main():
    try:
        # Nhập ngày và tháng từ người dùng
        ngay = int(input("Nhập vào ngày mà bạn muốn tìm: "))
        thang = int(input("Nhập vào tháng bạn muốn tìm: "))

        # Tính số ngày từ đầu năm
        so_ngay_da_qua = tinh_so_ngay_trong_nam(ngay, thang)
        print(f"Số ngày từ đầu năm đến ngày {ngay}/{thang} là: {so_ngay_da_qua}")

        # Tính số ngày còn lại trong năm
        so_ngay_con_lai = tinh_so_ngay_con_lai(ngay, thang)
        print(f"Số ngày còn lại trong năm từ ngày {ngay}/{thang} là: {so_ngay_con_lai}")

    except ValueError as e:
        print(f"Lỗi: {e}")


# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()