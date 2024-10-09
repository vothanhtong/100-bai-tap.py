# BÀI 17: Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
c=int(input("nhập vào số nguyên c: "))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print(a,b,c)