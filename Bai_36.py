# BÀI  36:Nhập vào A, tìm n nhỏ nhất sao cho
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A
a=float(input("nhập vào a: "))  # đây là số thực 
s=0
k=1
while s<=a:
    s+=1/k
    k+=1
print(k-1)