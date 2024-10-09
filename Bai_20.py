# BÀI 20 :Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày
a=int(input("nhập vào tháng mà bạn muốn tìm: "))
b=int(input("nhập vào năm bạn muốn tìm:  "))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("tháng có 31 ngày: ")
elif a==4 or a==6 or a==9 or a==11:
    print("tháng có 30 ngày: ")
else: 
    if  (b%400==0) or (b%4==0 and b%100!=0):
        print("tháng có 29 ngày: ")
    else:
        print("tháng có 28 ngày: ")