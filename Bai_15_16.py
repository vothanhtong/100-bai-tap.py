# BÀI 15 và 16 :))) :Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
c=int(input("nhập vào số nguyên c: "))
if (a+b>c and b+c>a and a+c>b):
    if a==b==c :
        print("đây là tam giác điều: ")
    elif  a==b or a==c or b==c: 
        if a**2+b**2 == c**2 or a**2+c**2 == b**2 or c**2+b**2 == a**2 :
            print("đây là tam giác vuông cân: ")
        else:
            print("đây là tam giác cân: ")
    elif a**2+b**2 == c**2 or a**2+c**2 == b**2 or c**2+b**2 == a**2 :
        print("đây là tam giác vuông: ")
    else:
        print("đây là tam giác thường: ")
else:
    print("đây không cấu tạo thành tam giác: ")