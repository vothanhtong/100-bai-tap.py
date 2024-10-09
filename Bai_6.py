# BÀI 6: Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
# CÁCH 1: 
a=int(input("nhập vào số nguyên a: "))
if a%5==0 and not 20<=a<=70:
    print("TRUE")
else:

    print("FALSE")
# # CÁCH 2:
a=int(input("nhập vào số nguyên a: "))
print(a%5==0 and not 20<=a<=70)