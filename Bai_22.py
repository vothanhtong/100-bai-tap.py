# BÀI 22: Nhập điểm toán, văn, anh.
# Nếu điểm đúng quy tắc (trong khoảng từ 0 - 10), ta tính điểm trung bình rồi tiến hành xét:
# Nếu điểm trung bình lớn hơn hoặc bằng 8, toán hoặc văn lớn hơn hoặc bằng 8 và không có điểm nào dưới 6.5 thì in ra “Học sinh giỏi”
# Nếu không đủ điều kiện học sinh giỏi ta xét nếu điểm trung bình lớn hơn hoặc bằng 6.5, 
# toán hoặc văn lớn hơn hoặc bằng 6.5 và không có điểm nào dưới 5 thì in ra “Học sinh khá”
# Nếu không đủ điều kiện học sinh khá ta xét nếu điểm trung bình lớn hơn hoặc bằng 5, toán hoặc văn lớn hơn
#  hoặc bằng 5 và không có điểm nào dưới 3.5 thì in ra “Học sinh trung bình”
# Nếu không đủ điều kiện học sinh trung bình ta xét nếu điểm trung bình lớn hơn hoặc bằng 3.5, toán hoặc văn lớn 
# hơn hoặc bằng 3.5 và không có điểm nào dưới 2 thì in ra “Học sinh yếu”
# Nếu không đủ điều kiện học sinh yếu ta in ra “Học sinh kém”
a=int(input("nhập điểm toán: "))
b=int(input("nhập điểm văn: "))
c=int(input("nhập điểm anh: "))
if (0<=a<=10,0<=b<=10,0<=c<=10):
     dtb= (a+b+c)/3
     if dtb>=8 and (a>=8 or b>=8 ) and (a>=6.5,b>=6.5,c>=6.5):
          print("học sinh giỏi:")
     elif dtb >=6.5 and (a>=6.5 or b>=6.5 ) and (a>=5,b>=5,c>=5):
        print("học sinh khá: ")
     elif dtb >=5 and (a>=5 or b>=5 ) and (a>=3.5,b>=3.5,c>=3.5):
        print("học sinh trung bình: ")
     elif dtb >=3.5 and (a>=3.5 or b>=3.5 ) and (a>=2,b>=2,c>=2):
         print ("học sinh yếu: ")
     else: 
         print("học sinh kém: ")
else: 
    print("bạn đã nhập sai: ")
# C2
#    
    # BÀI 22: Nhập điểm toán, văn, anh.
# Xét loại học sinh dựa trên điểm trung bình và các điều kiện cụ thể.

# Nhập điểm
toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
anh = float(input("Nhập điểm Anh: "))

# Kiểm tra điểm có hợp lệ hay không
if 0 <= toan <= 10 and 0 <= van <= 10 and 0 <= anh <= 10:
    # Tính điểm trung bình
    dtb = (toan + van + anh) / 3

    # Xét loại học sinh
    if dtb >= 8 and (toan >= 8 or van >= 8) and min(toan, van, anh) >= 6.5:
        print("Học sinh giỏi")
    elif dtb >= 6.5 and (toan >= 6.5 or van >= 6.5) and min(toan, van, anh) >= 5:
        print("Học sinh khá")
    elif dtb >= 5 and (toan >= 5 or van >= 5) and min(toan, van, anh) >= 3.5:
        print("Học sinh trung bình")
    elif dtb >= 3.5 and (toan >= 3.5 or van >= 3.5) and min(toan, van, anh) >= 2:
        print("Học sinh yếu")
    else:
        print("Học sinh kém")
else:
    print("Bạn đã nhập sai điểm. Điểm phải nằm trong khoảng từ 0 đến 10.")