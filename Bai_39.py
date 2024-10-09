# BÀI  39:Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ
s=int(input("nhập vào n: "))
demchan=demle=0
while s != 0:
    a=s%10
    s=s//10
    if a%2==0:
        demchan+=1
    else:
        demle+=1
print("tổng chữ số chẵn là: ",demchan)
print("tổng chữ số lẻ là: ",demle)