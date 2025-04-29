# BÀI 46: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số
chuoi = input("nhập vào một chuỗi: ")
demhoa = demthuong = demso = 0
for i in chuoi :
    if i.isupper():
        demhoa += 1
    elif i.islower():
        demthuong += 1
    elif i.isnumeric ():
        demso += 1 
print("số ký tự in hoa là: ",demhoa)   
print("số ký tự in thường là: ",demthuong)   
print("số ký tự số là: ",demso)  
def dem_ky_tu(chuoi):
    """
    Đếm số ký tự in hoa, in thường và số trong chuỗi.
    Args:
        chuoi (str): Chuỗi cần đếm.
    Returns:
        tuple: Số ký tự in hoa, in thường và số.
    """
    dem_hoa = dem_thuong = dem_so = 0
    for i in chuoi:
        if i.isupper():
            dem_hoa += 1
        elif i.islower():
            dem_thuong += 1
        elif i.isnumeric():
            dem_so += 1
    return dem_hoa, dem_thuong, dem_so


def dem_ky_tu_dac_biet(chuoi):
    """
    Đếm số ký tự đặc biệt trong chuỗi.
    Args:
        chuoi (str): Chuỗi cần đếm.
    Returns:
        int: Số ký tự đặc biệt.
    """
    return sum(1 for i in chuoi if not i.isalnum() and not i.isspace())


def kiem_tra_chuoi_hop_le(chuoi):
    """
    Kiểm tra xem chuỗi có phải chỉ chứa chữ cái và số không.
    Args:
        chuoi (str): Chuỗi cần kiểm tra.
    Returns:
        bool: True nếu chuỗi chỉ chứa chữ cái và số, ngược lại False.
    """
    return chuoi.isalnum()


def ky_tu_xuat_hien_nhieu_nhat(chuoi):
    """
    Tìm ký tự xuất hiện nhiều nhất trong chuỗi.
    Args:
        chuoi (str): Chuỗi cần kiểm tra.
    Returns:
        tuple: Ký tự xuất hiện nhiều nhất và số lần xuất hiện.
    """
    if not chuoi:
        return None, 0
    ky_tu_tan_suat = {}
    for i in chuoi:
        ky_tu_tan_suat[i] = ky_tu_tan_suat.get(i, 0) + 1
    ky_tu_max = max(ky_tu_tan_suat, key=ky_tu_tan_suat.get)
    return ky_tu_max, ky_tu_tan_suat[ky_tu_max]


def main():
    chuoi = input("Nhập vào một chuỗi: ")

    # Đếm số ký tự in hoa, in thường và số
    dem_hoa, dem_thuong, dem_so = dem_ky_tu(chuoi)
    print(f"Số ký tự in hoa là: {dem_hoa}")
    print(f"Số ký tự in thường là: {dem_thuong}")
    print(f"Số ký tự số là: {dem_so}")

    # Đếm số ký tự đặc biệt
    dem_dac_biet = dem_ky_tu_dac_biet(chuoi)
    print(f"Số ký tự đặc biệt là: {dem_dac_biet}")

    # Kiểm tra chuỗi có hợp lệ không
    hop_le = kiem_tra_chuoi_hop_le(chuoi)
    print(f"Chuỗi chỉ chứa chữ cái và số: {hop_le}")

    # Tìm ký tự xuất hiện nhiều nhất
    ky_tu_max, tan_suat = ky_tu_xuat_hien_nhieu_nhat(chuoi)
    if ky_tu_max:
        print(f"Ký tự xuất hiện nhiều nhất là: '{ky_tu_max}' với {tan_suat} lần")
    else:
        print("Chuỗi rỗng, không có ký tự nào.")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()