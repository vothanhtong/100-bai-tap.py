# BÀI TẬP LUYỆN TẬP & ỨNG DỤNG
# Bài 86: Một nhà hàng có các món ăn: Gà rán, hamburger, cocacola
# Giá của gà rán là: 30.000đ
# Giá của hamburger là: 25.000đ
# Giá của cocacola là: 10.000đ
# Yêu cầu người dùng nhập vào số lượng từng món ăn.
# Sau đó in ra hóa đơn theo dạng như sau:
# Chào mừng các bạn đến với nhà hàng thức ăn nhanh!
# Mời bạn nhập số lượng từng món ăn:
# Gà rán: 2
# Hamburger: 3
# Cocacola: 5
# Hóa đơn:
# Gà rán             30.000đ x 2
# Hamburger          25.000đ x 3
# Cocacola           10.000đ x 5
# Tổng:
# Gà rán             60.000đ
# Hamburger          75.000đ
# Cocacola           50.000đ
# Tổng trước thuế    185.000đ
# Thuế(5%)           9.250đ
# Tổng sau thuế      194.250đ
# Phần bên trái có số ký tự là 20 ký tự

# def in_hoa_don():
#     # Giá của các món ăn
#     menu = {
#         'Gà rán': 30000,
#         'Hamburger': 25000,
#         'Cocacola': 10000
#     }

#     # Yêu cầu người dùng nhập số lượng từng món ăn
#     print("Chào mừng các bạn đến với nhà hàng thức ăn nhanh!")
#     print("Mời bạn nhập số lượng từng món ăn:")
#     so_luong_ga_ran = int(input("Gà rán: "))
#     so_luong_hamburger = int(input("Hamburger: "))
#     so_luong_cocacola = int(input("Cocacola: "))

#     # Tính tổng tiền từng món
#     tong_ga_ran = menu['Gà rán'] * so_luong_ga_ran
#     tong_hamburger = menu['Hamburger'] * so_luong_hamburger
#     tong_cocacola = menu['Cocacola'] * so_luong_cocacola

#     # Tổng trước thuế
#     tong_truoc_thue = tong_ga_ran + tong_hamburger + tong_cocacola

#     # Tính thuế (5%)
#     thue = tong_truoc_thue * 0.05
#     # Tổng sau thuế
#     tong_sau_thue = tong_truoc_thue + thue
#     # In hóa đơn
#     print("\nHóa đơn:")
#     print(f"{'Gà rán':<20}{menu['Gà rán']:>6,}đ x {so_luong_ga_ran}")
#     print(f"{'Hamburger':<20}{menu['Hamburger']:>6,}đ x {so_luong_hamburger}")
#     print(f"{'Cocacola':<20}{menu['Cocacola']:>6,}đ x {so_luong_cocacola}")
#     print("\nTổng:")
#     print(f"{'Gà rán':<20}{tong_ga_ran:>6,}đ")
#     print(f"{'Hamburger':<20}{tong_hamburger:>6,}đ")
#     print(f"{'Cocacola':<20}{tong_cocacola:>6,}đ")
#     print(f"{'Tổng trước thuế':<20}{tong_truoc_thue:>6,}đ")
#     print(f"{'Thuế(5%)':<20}{thue:>6,.0f}đ")
#     print(f"{'Tổng sau thuế':<20}{tong_sau_thue:>6,.0f}đ")
# # Gọi hàm để in hóa đơn
# in_hoa_don()
