# BÀI 5:  Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
# cách 1:
a=int(input("nhập số nguyên a: "))
if a %3 == 0 and 50<= a <=100:
    print("TRUE")
else:
    print("FALSE")
# cách 2:
a=int(input("nhập vào số nguyên a: "))
print(a%3==0 and 50<=a<=100)