# BÀI  29:Nhập vào số nguyên dương a, in toàn bộ ước của a
a=int(input("nhập vào a: "))
for i in range(1,a+1):
    if a%i==0:
        print(i)