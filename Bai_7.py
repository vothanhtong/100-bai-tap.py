# BÀI 7: Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
print(a%2==0 or b%2==0 )
# # cách 2:
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
if a%2==0 or b%2==0: 
    print("TRUE")
else:
    print("FALSE")