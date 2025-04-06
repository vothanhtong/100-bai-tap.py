# BÀI 12: Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c
# Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
c=int(input("nhập vào số nguyên c: "))
d=(a+b)**c 
print(d)
if 100<=d<=200:
    print("TRUE")
else:
    print("FALSE")


# BÀI 13: Nhập vào 3 số x, y, z. Tính và in ra k = (x * y) + z
# Nếu k là số chẵn thì in ra True, ngược lại in ra False
x = int(input("Nhập vào số nguyên x: "))
y = int(input("Nhập vào số nguyên y: "))
z = int(input("Nhập vào số nguyên z: "))
k = (x * y) + z
print("Giá trị của k là:", k)
if k % 2 == 0:
    print("TRUE")
else:
    print("FALSE")