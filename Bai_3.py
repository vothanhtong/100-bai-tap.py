# BÀI 3:Nhập vào nhiệt độ c, in ra nhiệt độ F
a=float(input("nhập vào nhiệt độ c: "))
n=(a*1.8)+32
print("nhiệt độ f là: ",n)

# Bài 4 : nhập nhiệt độ 
f = int(input("nhập nhiệt dộ c :"))
c = (f -32 )/1.8
print ("nhiệt độ c là : ", c)

#  BÀI 5: Nhập vào nhiệt độ C, kiểm tra xem có phải nhiệt độ đóng băng của nước không
c = float(input("Nhập vào nhiệt độ C: "))
if c == 0:
    print("Đây là nhiệt độ đóng băng của nước.")
else:
    print("Đây không phải là nhiệt độ đóng băng của nước.")

# BÀI 6: Nhập vào nhiệt độ C, kiểm tra xem có phải nhiệt độ sôi của nước không
c = float(input("Nhập vào nhiệt độ C: "))
if c == 100:
    print("Đây là nhiệt độ sôi của nước.")
else:
    print("Đây không phải là nhiệt độ sôi của nước.")

# BÀI 7: Nhập vào nhiệt độ C, kiểm tra xem nhiệt độ đó là nóng, lạnh hay bình thường
c = float(input("Nhập vào nhiệt độ C: "))
if c < 20:
    print("Nhiệt độ này là lạnh.")
elif 20 <= c <= 30:
    print("Nhiệt độ này là bình thường.")
else:
    print("Nhiệt độ này là nóng.")