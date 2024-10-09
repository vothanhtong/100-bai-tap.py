# BÀI  41: Nhập vào một số nguyên dương n, kiểm tra xem n có phải là số dạng 2^k hay không
n=int(input("nhập số nguyên n: "))
n0=n
while n%2==0:
    n=n/2
if n==1:
    print(n0,"là số dạng 2^k: ")
else:
    print(n0,"không phải số dạng 2^k: ")