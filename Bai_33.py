# BÀI  33:Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không
a=int(input("nhập số nguyên a: "))
if a>1 :
    dem=0
    for i in range (1,a+1):
        if a%i==0:
            dem+=1
    if dem==2:
        print("đây là số nguyên tố: ")
    else:
        print("không phải số nguyên tố: ")
else:
     print("không phải số nguyên tố: ")