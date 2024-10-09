# BÀI 47:Nhập vào một chuỗi, hãy tách toàn bộ ký tự số trong chuỗi ra rồi tính tổng của chúng
# VD: Nhập chuỗi: abd45ecf47wde3s1
# Tổng: 4 + 5 + 4 + 7 + 3 + 1 = 24
chuoi = input("nhập vào chuỗi: ")
tong = 0
for i in chuoi:
    if i.isnumeric():
        tong += int(i)
print(tong) 