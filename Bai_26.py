# BÀI  26:Nhập vào số nguyên dương a, in ra bảng cửu chương của a
a=int(input("nhập vào số nguyên dương a để in ra bảng cửu chương a: "))
for i in range(1,10+1):
    print( a, "x" ,i, "=", a*i)