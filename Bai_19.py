# BÀI 19: Giải và biện luận phương trình ax^2 + bx + c = 0
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
c=int(input("nhập vào số nguyên c: "))
print("phương trình"+ str(a) +"x^2 + " + str(b)+"x+"+ str(c)+ "=0")
if a==0:
    if b==0:
        if c==0:
            print("phương trình vô số nghiệm: ")
        else:
            print("phương trình vô nghiệm: ")
    else: 
        print("phương trình có một nghiệm là:",-c/b)
else:
    denta = b**2 - 4*a*c
    if denta>0:
        candenta= denta**0.5
        x1= (-b +candenta)/(2*a)
        x2= (-b -candenta)/(2*a)
        print("phương trình này có hai nghiệm phân biệt là: ",x1, "và" ,x2)
    elif denta==0:
        print("phương trình có nghiệm kép x1=x2:  ",-b/(a*a))
    else:
        print("phương trình vô nghiệm: ")