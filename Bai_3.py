# BÀI 3: Nhập vào nhiệt độ C, in ra nhiệt độ F
celsius = float(input("Nhập vào nhiệt độ C: "))
fahrenheit = (celsius * 1.8) + 32
print("Nhiệt độ F là:", fahrenheit)

# BÀI 4: Nhập nhiệt độ F, chuyển đổi sang C
fahrenheit = int(input("Nhập nhiệt độ F: "))
celsius = (fahrenheit - 32) / 1.8
print("Nhiệt độ C là:", celsius)

# BÀI 5: Nhập vào nhiệt độ C, kiểm tra xem có phải nhiệt độ đóng băng của nước không
celsius = float(input("Nhập vào nhiệt độ C: "))
if celsius == 0:
    print("Đây là nhiệt độ đóng băng của nước.")
else:
    print("Đây không phải là nhiệt độ đóng băng của nước.")

# BÀI 6: Nhập vào nhiệt độ C, kiểm tra xem có phải nhiệt độ sôi của nước không
celsius = float(input("Nhập vào nhiệt độ C: "))
if celsius == 100:
    print("Đây là nhiệt độ sôi của nước.")
else:
    print("Đây không phải là nhiệt độ sôi của nước.")

# BÀI 7: Nhập vào nhiệt độ C, kiểm tra xem nhiệt độ đó là nóng, lạnh hay bình thường
celsius = float(input("Nhập vào nhiệt độ C: "))
if celsius < 20:
    print("Nhiệt độ này là lạnh.")
elif 20 <= celsius <= 30:
    print("Nhiệt độ này là bình thường.")
else:
    print("Nhiệt độ này là nóng.")