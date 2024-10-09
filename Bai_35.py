# BÀI  35: Nhập n
# Cho S(k) = 1 + 2 + 3 + … + k
# Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n
a=int(input("nhập số nguyên a: "))
s=0
k=1
while s<a:
    s+=k
    k+=1
print(k-2)