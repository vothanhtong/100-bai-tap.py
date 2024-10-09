# BÀI  27:Viết chương trình in ra hình tam giác có độ cao h được nhập từ bàn phím
a=int(input("nhập vào độ cao h: "))
khoangtrangngoai= a-1
khoangtrangtrong=1
for i in range (a):
    if i==0:
        print(" " * khoangtrangngoai + "*")
    elif i<a -1:
        print(" " * khoangtrangngoai + "*" + " " * khoangtrangtrong + "*")
        khoangtrangtrong += 2
    else:
        print("*" * (a*2-1))
    khoangtrangngoai -= 1