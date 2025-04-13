def nhap_so_luong(menu):
    """
    Hàm yêu cầu người dùng nhập số lượng từng món ăn.
    Args:
        menu (dict): Menu chứa tên món ăn và giá tiền.
    Returns:
        dict: Số lượng từng món ăn.
    """
    print("Chào mừng các bạn đến với nhà hàng thức ăn nhanh!")
    print("Mời bạn nhập số lượng từng món ăn:")
    so_luong = {}
    for mon in menu:
        while True:
            try:
                sl = int(input(f"{mon}: "))
                if sl < 0:
                    raise ValueError("Số lượng phải là số nguyên không âm.")
                so_luong[mon] = sl
                break
            except ValueError as e:
                print(f"Lỗi: {e}. Vui lòng nhập lại.")
    return so_luong


def tinh_tong_tien(menu, so_luong):
    """
    Hàm tính tổng tiền từng món và tổng tiền trước thuế.
    Args:
        menu (dict): Menu chứa tên món ăn và giá tiền.
        so_luong (dict): Số lượng từng món ăn.
    Returns:
        dict: Tổng tiền từng món.
        float: Tổng tiền trước thuế.
    """
    tong_tien_tung_mon = {mon: menu[mon] * so_luong[mon] for mon in menu}
    tong_truoc_thue = sum(tong_tien_tung_mon.values())
    return tong_tien_tung_mon, tong_truoc_thue


def in_hoa_don(menu, so_luong, tong_tien_tung_mon, tong_truoc_thue, thue_suat):
    """
    Hàm in hóa đơn.
    Args:
        menu (dict): Menu chứa tên món ăn và giá tiền.
        so_luong (dict): Số lượng từng món ăn.
        tong_tien_tung_mon (dict): Tổng tiền từng món.
        tong_truoc_thue (float): Tổng tiền trước thuế.
        thue_suat (float): Thuế suất.
    """
    thue = tong_truoc_thue * thue_suat
    tong_sau_thue = tong_truoc_thue + thue

    print("\nHÓA ĐƠN".center(40, "-"))
    for mon in menu:
        print(f"{mon:<20}{menu[mon]:>6,}đ x {so_luong[mon]:<2} = {tong_tien_tung_mon[mon]:>6,}đ")
    print("-" * 40)
    print(f"{'Tổng trước thuế':<30}{tong_truoc_thue:>6,}đ")
    print(f"{'Thuế (5%)':<30}{thue:>6,.0f}đ")
    print(f"{'Tổng sau thuế':<30}{tong_sau_thue:>6,.0f}đ")
    print("-" * 40)


def main():
    # Giá của các món ăn
    menu = {
        'Gà rán': 30000,
        'Hamburger': 25000,
        'Cocacola': 10000
    }

    # Nhập số lượng từng món ăn
    so_luong = nhap_so_luong(menu)

    # Tính tổng tiền
    tong_tien_tung_mon, tong_truoc_thue = tinh_tong_tien(menu, so_luong)

    # In hóa đơn
    in_hoa_don(menu, so_luong, tong_tien_tung_mon, tong_truoc_thue, thue_suat=0.05)


# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()