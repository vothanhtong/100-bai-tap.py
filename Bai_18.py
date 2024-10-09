# BÀI 18: Giải và biện luận phương trình ax + b = 0
a = int(input("nhập vào số nguyên a: "))
b = int(input("nhập vào số nguyên b: "))
print ("phương trình" + str(a) + "x+" + str(b)+"=0" )
if a == 0:
    if b == 0:
        print("phương trình vô số nghiệm: ")
    else:
        print("phương trình vô nghiệm: ")
else:
    print("nghiệm của phương trình là: ",-b/a)  