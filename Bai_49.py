# BÀI 49:Nhập vào một chuỗi, hãy tách toàn bộ con số trong chuỗi ra rồi tính tổng của chúng
# VD: Nhập chuỗi: abd45ecf47wde3s1
# Tổng: 45 + 47 + 3 + 1 = 96
chuoi = input("nhập vào một chuỗi: ")
chuoitam = ""
tong = 0
for i in chuoi :
    if i.isnumeric():
        chuoitam += i 
    else:
        if chuoitam != "":
            tong += int(chuoitam)
            chuoitam = ""
if chuoitam != "":
    tong += int(chuoitam)
print(tong)

import re

def tinh_tong_cac_so_trong_chuoi(chuoi):
    """
    Tách toàn bộ các số trong chuỗi và tính tổng của chúng.
    Args:
        chuoi (str): Chuỗi chứa các số và ký tự khác.
    Returns:
        int: Tổng các số trong chuỗi.
    """
    # Sử dụng regex để tìm tất cả các số trong chuỗi
    cac_so = re.findall(r'\d+', chuoi)
    # Tính tổng các số
    return sum(map(int, cac_so))

def main():
    # Nhập chuỗi từ người dùng
    chuoi = input("Nhập vào một chuỗi: ")
    # Tính tổng các số trong chuỗi
    tong = tinh_tong_cac_so_trong_chuoi(chuoi)
    print(f"Tổng các số trong chuỗi là: {tong}")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()