# BÀI  39:Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ
s=int(input("nhập vào n: "))
demchan=demle=0
while s != 0:
    a=s%10
    s=s//10
    if a%2==0:
        demchan+=1
    else:
        demle+=1
print("tổng chữ số chẵn là: ",demchan)
print("tổng chữ số lẻ là: ",demle)

def dem_chan_le(n):
    """
    Đếm số chữ số chẵn và lẻ trong số nguyên dương n.
    Args:
        n (int): Số nguyên dương cần đếm.
    Returns:
        tuple: Số lượng chữ số chẵn và lẻ.
    """
    dem_chan = dem_le = 0
    while n != 0:
        a = n % 10
        n //= 10
        if a % 2 == 0:
            dem_chan += 1
        else:
            dem_le += 1
    return dem_chan, dem_le


def tong_chan_le(n):
    """
    Tính tổng các chữ số chẵn và lẻ trong số nguyên dương n.
    Args:
        n (int): Số nguyên dương cần tính tổng.
    Returns:
        tuple: Tổng các chữ số chẵn và lẻ.
    """
    tong_chan = tong_le = 0
    while n != 0:
        a = n % 10
        n //= 10
        if a % 2 == 0:
            tong_chan += a
        else:
            tong_le += a
    return tong_chan, tong_le


def tim_chu_so_lon_nhat_va_nho_nhat(n):
    """
    Tìm chữ số lớn nhất và nhỏ nhất trong số nguyên dương n.
    Args:
        n (int): Số nguyên dương cần tìm.
    Returns:
        tuple: Chữ số lớn nhất và nhỏ nhất.
    """
    chu_so_lon_nhat = 0
    chu_so_nho_nhat = 9
    while n != 0:
        a = n % 10
        n //= 10
        chu_so_lon_nhat = max(chu_so_lon_nhat, a)
        chu_so_nho_nhat = min(chu_so_nho_nhat, a)
    return chu_so_lon_nhat, chu_so_nho_nhat


def main():
    try:
        # Nhập số nguyên dương từ người dùng
        n = int(input("Nhập vào số nguyên dương n: "))
        if n <= 0:
            raise ValueError("Số phải là số nguyên dương lớn hơn 0.")

        # Đếm số chữ số chẵn và lẻ
        dem_chan, dem_le = dem_chan_le(n)
        print(f"Tổng chữ số chẵn là: {dem_chan}")
        print(f"Tổng chữ số lẻ là: {dem_le}")

        # Tính tổng các chữ số chẵn và lẻ
        tong_chan, tong_le = tong_chan_le(n)
        print(f"Tổng các chữ số chẵn là: {tong_chan}")
        print(f"Tổng các chữ số lẻ là: {tong_le}")

        # Tìm chữ số lớn nhất và nhỏ nhất
        chu_so_lon_nhat, chu_so_nho_nhat = tim_chu_so_lon_nhat_va_nho_nhat(n)
        print(f"Chữ số lớn nhất là: {chu_so_lon_nhat}")
        print(f"Chữ số nhỏ nhất là: {chu_so_nho_nhat}")

    except ValueError as e:
        print(f"Lỗi: {e}")


# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()