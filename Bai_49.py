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