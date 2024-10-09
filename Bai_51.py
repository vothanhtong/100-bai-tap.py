# BÀI 51: Nhập vào một số nguyên, hãy chuyển số sang chuỗi, rồi đặt dấu chấm phân tách mỗi 3 chữ số (phân cách phần ngàn) rồi in ra màn hình
# VD: Nhập số: 375469485
# Đổi sang chuỗi rồi in ra: 375.469.485
a = int(input("nhập vào số nguyên: "))
a = str(a)
i = len(a) - 3      
while i > 0:
    a = a[:i] + "." + a[i:]
    i -= 3
print(a)