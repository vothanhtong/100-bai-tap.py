# BÀI 40:Nhập vào số nguyên dương n, tính tổng các chữ số của n
s=int(input("nhập vào số bất kỳ: "))
a=0
while s!=0:
    n=s%10
    s=s//10 
    a += n
print("tổng các chữ số bằng: ",a)