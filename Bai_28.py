# BÀI  28: Nhập vào n
# Tính S = 1 + 2 + 3 + 4 + … + n
n=int(input("nhập vào số nguyên n: "))
s=0
for i in range (1,n+1):
    s+=i
print(s)