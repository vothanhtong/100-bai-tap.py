# BÀI  32:Nhập vào số nguyên dương a và b, in ước chung lớn nhất của a và b
a=int(input("nhập vào a: "))
b=int(input("nhập vào b: "))
ucln=1
for i in range (1,a+1):
    if i>b:
        break
    if a%i==0 and b%i==0:
        ucln=i
print(ucln)