# BÀI TẬP NHẬP LIỆU VÀ TOÁN TỬ CƠ BẢN
# BÀI 1: Nhập vào số n, hãy nhân n lên cho 3, rồi cộng 1 sau đó in kết quả ra màn hình
a=int(input("nhập vào số nguyên a: "))
n=(a*3)+1
print("khi a nhân cho ba và cộng cho một là: ",n)
# BÀI 2: Nhập vào số n, hãy mũ 2 rồi chia cho 3, sau đó in kết quả ra màn hình
a=int(input("nhập vào số nguyên a: "))
n=(a**2)/3
print("số in ra màng hình là: ",n)
# BÀI 3:Nhập vào nhiệt độ c, in ra nhiệt độ F
a=float(input("nhập vào nhiệt độ c: "))
n=(a*1.8)+32
print("nhiệt độ f là: ",n)
# BÀI 4:Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False
a=int(input("nhập vào số nguyên a: "))
if a%2==0:
    print("TRUE")
else:
    print("FALSE")
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
# BÀI 6: Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
# CÁCH 1: 
a=int(input("nhập vào số nguyên a: "))
if a%5==0 and not 20<=a<=70:
    print("TRUE")
else:

    print("FALSE")
# CÁCH 2:
a=int(input("nhập vào số nguyên a: "))
print(a%5==0 and not 20<=a<=70)
# BÀI 7: Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
print(a%2==0 or b%2==0 )
# cách 2:
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
if a%2==0 or b%2==0: 
    print("TRUE")
else:
    print("FALSE")
# BÀI 8: Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False
a=float(input("nhập vào một số a: "))
b=round(a)
print(a==b )
# BÀI 9:Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False
a=int(input("nhập số nguyên a:  "))
cana=a**0.5
print(cana==round(cana))
# BÀI 10:Nhập vào lương tháng này nhận được, ta phải đưa cho vợ 90% số tiền lương đó. Hãy in ra lương ta giữ lại
a=int(input("nhập vào lương tháng này bạn nhận được: "))
print("lương giữ lại còn: ",a*0.1)
# BÀI 11:Nhập vào 3 số a, b, c. In ra kết quả là tổng của ba số đó
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
c=int(input("nhập vào số nguyên c: "))
tong=a+b+c
print("tổng ba số a,b,a là: ",tong)
# BÀI 12: Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c
# Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
c=int(input("nhập vào số nguyên c: "))
d=(a+b)**c 
print(d)
if 100<=d<=200:
    print("TRUE")
else:
    print("FALSE")
# BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN
# BÀI 13:Nhập vào số nguyên dương a, nếu a lớn hơn 10 thì ta in ra đây là số lớn hơn 10
a=int(input("nhập vào số nguyên a: "))
if a>10 :
    print("đây là số lớn hơn 10: ")
else:
    print("đây là số nhỏ hơn 10: ")
# BÀI 14: Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ
a=int(input("nhập vào số nguyên dương a: "))
print("số này đặc biệt: ")
if a%2==0:
    print("đây là số chẵn ")
else:
    print("đây là số lẻ: ")
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
# BÀI 17: Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
c=int(input("nhập vào số nguyên c: "))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print(a,b,c)
# BÀI 18: Giải và biện luận phương trình ax + b = 0
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
print ("phương trình"+str(a)+"x+"+str(b)+"=0" )
if a==0:
    if b==0:
        print("phương trình vô số nghiệm: ")
    else:
        print("phương trình vô nghiệm: ")
else:
    print("nghiệm của phương trình là: ",-b/a)        
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
# BÀI 21:Ngày vào ngày, tháng. Hãy tính và in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày 
# (giả sư năm đó không phải là năm nhuận)
a=int(input("nhập vào ngày mà bạn muốn tìm: "))
b=int(input("nhập vào tháng bạn muốn tìm:  "))
if b<=8:
    sothang30ngay=(b-1)//2
    sothang31ngay=b//2
else:
    sothang30ngay=b//2-1
    sothang31ngay=(b+1)//2
songay=a+sothang30ngay*30 +sothang31ngay*31
if b>2:
    songay-=2
print (songay)
# BÀI 22: Nhập điểm toán, văn, anh.
# Nếu điểm đúng quy tắc (trong khoảng từ 0 - 10), ta tính điểm trung bình rồi tiến hành xét:
# Nếu điểm trung bình lớn hơn hoặc bằng 8, toán hoặc văn lớn hơn hoặc bằng 8 và không có điểm nào dưới 6.5 thì in ra “Học sinh giỏi”
# Nếu không đủ điều kiện học sinh giỏi ta xét nếu điểm trung bình lớn hơn hoặc bằng 6.5, 
# toán hoặc văn lớn hơn hoặc bằng 6.5 và không có điểm nào dưới 5 thì in ra “Học sinh khá”
# Nếu không đủ điều kiện học sinh khá ta xét nếu điểm trung bình lớn hơn hoặc bằng 5, toán hoặc văn lớn hơn
#  hoặc bằng 5 và không có điểm nào dưới 3.5 thì in ra “Học sinh trung bình”
# Nếu không đủ điều kiện học sinh trung bình ta xét nếu điểm trung bình lớn hơn hoặc bằng 3.5, toán hoặc văn lớn 
# hơn hoặc bằng 3.5 và không có điểm nào dưới 2 thì in ra “Học sinh yếu”
# Nếu không đủ điều kiện học sinh yếu ta in ra “Học sinh kém”
a=int(input("nhập điểm toán: "))
b=int(input("nhập điểm văn: "))
c=int(input("nhập điểm anh: "))
if (0<=a<=10,0<=b<=10,0<=c<=10):
     dtb= (a+b+c)/3
     if dtb>=8 and (a>=8 or b>=8 ) and (a>=6.5,b>=6.5,c>=6.5):
          print("học sinh giỏi:")
     elif dtb >=6.5 and (a>=6.5 or b>=6.5 ) and (a>=5,b>=5,c>=5):
        print("học sinh khá: ")
     elif dtb >=5 and (a>=5 or b>=5 ) and (a>=3.5,b>=3.5,c>=3.5):
        print("học sinh trung bình: ")
     elif dtb >=3.5 and (a>=3.5 or b>=3.5 ) and (a>=2,b>=2,c>=2):
         print ("học sinh yếu: ")
     else: 
         print("học sinh kém: ")
else: 
    print("bạn đã nhập sai: ")
# BÀI TẬP VÒNG LẶP FOR
# BÀI  23: In 10 lần chữ hello ra màn hình
for i in range (1,10+1):
    print("In 10 lần chữ hello ra màn hình")
# BÀI  24: In các số lẻ dương bé hơn 100
for i in range(1,100,2):
    print(i)
# BÀI  25:In các số chẵn chia hết cho 3 bé hơn 100
for i in range(1,100,):
    if i%3==0 and i%2==0:
        print(i)
# BÀI  26:Nhập vào số nguyên dương a, in ra bảng cửu chương của a
a=int(input("nhập vào số nguyên dương a để in ra bảng cửu chương a: "))
for i in range(1,10+1):
    print( a, "x" ,i, "=", a*i)
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
# BÀI  28: Nhập vào n
# Tính S = 1 + 2 + 3 + 4 + … + n
n=int(input("nhập vào số nguyên n: "))
s=0
for i in range (1,n+1):
    s+=i
print(s)
# BÀI  29:Nhập vào số nguyên dương a, in toàn bộ ước của a
a=int(input("nhập vào a: "))
for i in range(1,a+1):
    if a%i==0:
        print(i)
# BÀI  30: Nhập vào số nguyên dương a, đếm số ước của a
a=int(input("nhập vào a: "))
dem=0
for i in range(1,a+1):
    if a%i==0:
        dem += 1
print(dem)
# BÀI  31:Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
a=int(input("nhập vào a: "))
b=int(input("nhập vào b: "))
for i in range (1,a+1):
    if i>b:
        break
    if a%i==0 and b%i==0:
        print(i)
# BÀI  32:Nhập vào số nguyên dương a và b, in ước chung lớn nhất của a và b
a=int(input("nhập vào a: "))
b=int(input("nhập vào b: "))
ucln=1
for i in range (1,a+1):
    if i>b:
        break
    if a%i==0 and b%i==0:
        ucln=i
print(ucln)
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
# BÀI TẬP VÒNG LẶP WHILE
# BÀI  34: Nhập vào số nguyên dương a, nếu nhập số âm thì yêu cầu nhập lại cho đến khi người dùng nhập đúng số dương
# Nếu người dùng nhập đúng số dương thì in ra “Bạn nhập đúng quy tắc”
a=int(input("nhập số nguyên a: "))
while a<=0:
    a=int(input("bạn nhập lại số nguyên: "))
print("bạn đã nhập đúng: ")
# BÀI  35: Nhập n
# Cho S(k) = 1 + 2 + 3 + … + k
# Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n
a=int(input("nhập số nguyên a: "))
s=0
k=1
while s<a:
    s+=k
    k+=1
print(k-2)
# BÀI  36:Nhập vào A, tìm n nhỏ nhất sao cho
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A
a=float(input("nhập vào a: "))  # đây là số thực 
s=0
k=1
while s<=a:
    s+=1/k
    k+=1
print(k-1)
# BÀI  37:Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1.
# Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập
a=int(input("nhập số nguyên a: "))
max= None
min= None
while a != -1:
    if max == None or max<a:
        max= a
    if min == None or min >a:
        min = a
    a=int(input("nhập số nguyên a: "))
print("số lớn nhất là: ",max)
print("số nhỏ nhất là: ",min)
# BÀI  38:Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số
a=int(input("nhập số nguyên a: "))
a=str(a)
dem= len(a)
print("số này có",dem,"chữ số.")
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
# BÀI 40:Nhập vào số nguyên dương n, tính tổng các chữ số của n
s=int(input("nhập vào số bất kỳ: "))
a=0
while s!=0:
    n=s%10
    s=s//10 
    a += n
print("tổng các chữ số bằng: ",a)
# BÀI  41: Nhập vào một số nguyên dương n, kiểm tra xem n có phải là số dạng 2^k hay không
n=int(input("nhập số nguyên n: "))
n0=n
while n%2==0:
    n=n/2
if n==1:
    print(n0,"là số dạng 2^k: ")
else:
    print(n0,"không phải số dạng 2^k: ")
# BÀI  43: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu từ (quy định là chuỗi không có ký tự đặc biệt,
# không số, không có dấu câu, chỉ có ký tự chữ và khoảng trắng)
a=input("nhập vào một chuỗi : ")
chuoi= a.count(" ")
print(chuoi+1)
# BÀI TẬP XỬ LÝ CHUỖI
# BÀI  44: Nhập vào một chuỗi, hãy in từ đầu tiên trong chuỗi
chuoi = input("nhập vào một chuỗi: ")
a = chuoi.find(" ")
tudautien = chuoi[:a]
print(tudautien)
# BÀI 44 B: không in ra từ cuối cùng của chuỗi 
chuoi = input("Nhập vào một chuỗi: ")
a = chuoi. rfind(" ")
chuoi0 = chuoi[ :a]
print(chuoi0)
chuoi = input("Nhập vào một chuỗi: ")
chuoi_list = chuoi.split(" ")  # Tách chuỗi thành các từ
chuoi0 = " ".join(chuoi_list[:-1])  # Nối lại các từ trừ từ cuối cùng
print(chuoi0)
# BÀI 45: Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên cách nhau một dấu phẩy, hãy tính tổng 3 số nguyên đó
chuoi = input("nhập vào một chuỗi có ba số nguyên: ")
a = chuoi.find(",")
b = chuoi.rfind(",")
so1 = int(chuoi[:a])
so2 = int(chuoi[a+1:b])
so3 = int(chuoi[b+1])
print(so1 + so2 + so3)
# BÀI 46: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số
chuoi = input("nhập vào một chuỗi: ")
demhoa = demthuong = demso = 0
for i in chuoi :
    if i.isupper():
        demhoa += 1
    elif i.islower():
        demthuong += 1
    elif i.isnumeric ():
        demso += 1 
print("số ký tự in hoa là: ",demhoa)   
print("số ký tự in thường là: ",demthuong)   
print("số ký tự số là: ",demso)   
# BÀI 47:Nhập vào một chuỗi, hãy tách toàn bộ ký tự số trong chuỗi ra rồi tính tổng của chúng
# VD:
# Nhập chuỗi: abd45ecf47wde3s1
# Tổng: 4 + 5 + 4 + 7 + 3 + 1 = 24
chuoi = input("nhập vào chuỗi: ")
tong = 0
for i in chuoi:
    if i.isnumeric():
        tong += int(i)
print(tong) 
# BÀI 49:Nhập vào một chuỗi, hãy tách toàn bộ con số trong chuỗi ra rồi tính tổng của chúng
# VD:
# Nhập chuỗi: abd45ecf47wde3s1
# Tổng: 45 + 47 + 3 + 1 = 96
chuoi = input("nhập vào một chuỗi: ")
chuoitam = ""
tong = 0
for i in chuoi :
    if i.isnumeric():
        chuoitam += i 
    else:
        if chuoitam != "":
            tong += int(chuoitam)
            chuoitam = ""
if chuoitam != "":
    tong += int(chuoitam)
print(tong)
# BÀI 50: Nhập vào một chuỗi, kiểm tra chuỗi đó có phải là một chuỗi mật khẩu mạnh hay không 
# (một chuỗi mật khẩu mạnh cần có ít nhất 1 ký tự đặc biệt, 1 ký tự in hoa, 1 con số, 1 chữ thường và độ dài phải lớn hơn 6)
chuoi = input ("nhập vào một chuỗi kiểm tra thử mật khẩu có mạnh hay không: ")
ktdodai = len(chuoi) > 6
ktdacbiet = ktinthuong = ktinhoa = ktso = False
for i in chuoi :
    if i.isnumeric():
        ktso = True
    elif i.isupper():
        ktinhoa = True
    elif i.islower():
        ktinthuong = True
    else:
        ktdacbiet = True
if ktdodai and ktso and ktinthuong and ktinhoa:
    print("đây là mật khẩu mạnh: ")
else:
    print("đây là mật khẩu yếu: ")
# BÀI 51: Nhập vào một số nguyên, hãy chuyển số sang chuỗi, rồi đặt dấu chấm phân tách mỗi 3 chữ số (phân cách phần ngàn) rồi in ra màn hình
# VD: Nhập số: 375469485
# Đổi sang chuỗi rồi in ra: 375.469.485
a = int(input("nhập vào số nguyên: "))
a = str(a)
i = len(a) - 3      
while i > 0:
    a = a[:i] + "." + a[i:]
    i -= 3
print(a)
# BÀI 52:Nhập vào chuỗi a và chuỗi b Hãy xóa chuỗi b trong chuỗi a rồi in lại chuỗi a ra màn hình (không dùng hàm replace)
# Ví dụ: Chuỗi a: "Xin chào mọi người!"
# Chuỗi b: "Xin chào"
# Sau khi xóa, chuỗi a: " mọi người!"
a = input("nhập vào chuỗi a: ")
b = input("nhập vào chuỗi b: ")
vt_dau = 0
vt_cuoi = len(b)    
while vt_cuoi <= len(a):
    if a[vt_dau:vt_cuoi] == b:
       a = a[:vt_dau] + a[vt_cuoi:]
    else:
        vt_dau += 1
        vt_cuoi += 1
print(a)

# BÀI TẬP XỬ LÝ LIST

# BÀI 53: Nhập vào list số nguyên
# Nhập vào một list số nguyên L, tìm và in ra giá trị lớn nhất trong L
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))
# Tìm và in ra giá trị lớn nhất
max_value = max(L)
print("Giá trị lớn nhất trong list là:", max_value)
# BÀI 54: Nhập vào một list số nguyên L, nhập vào 2 số nguyên dương a và b (a < b < len(L))
# Tìm và in ra số nhỏ nhất trong list từ vị trí a đến vị trí b
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Nhập hai số nguyên dương a và b (a < b < len(L))
a = int(input("Nhập số nguyên a (a < b < len(L)): "))
b = int(input("Nhập số nguyên b (a < b < len(L)): "))

# Kiểm tra điều kiện a < b < len(L)
if 0 <= a < b < len(L):
    # Tìm giá trị nhỏ nhất trong đoạn từ vị trí a đến vị trí b
    min_value = min(L[a:b+1])
    print(f"Giá trị nhỏ nhất từ vị trí {a} đến vị trí {b} trong list là:", min_value)
else:
    print("Giá trị a và b không hợp lệ.")
# BÀI 55: Nhập vào một list số nguyên L, hãy kiểm tra xem tất cả các phần tử trong mảng có bằng nhau hay không, nếu có thì in True, không có thì in False
# Nhập vào list số nguyên
# BÀI 56: Nhập vào một list số nguyên L, tìm và in ra giá trị dương đầu tiên của list, nếu không có giá trị dương, ta in ra -1
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Tìm giá trị dương đầu tiên trong list
first_positive = -1  # Khởi tạo giá trị mặc định là -1
for num in L:
    if num > 0:
        first_positive = num
        break

# In ra giá trị dương đầu tiên hoặc -1 nếu không có
print(first_positive)

# BÀI 57: Nhập vào một list L, hãy tìm và in ra giá trị âm lớn nhất trong/ L, nếu L không có giá trị âm thì ta in 0
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Lọc các giá trị âm trong list
negative_numbers = [num for num in L if num < 0]

# Tìm giá trị âm lớn nhất nếu có, nếu không thì in ra 0
if negative_numbers:
    max_negative = max(negative_numbers)
    print("Giá trị âm lớn nhất là:", max_negative)
else:
    print(0)

# BÀI 58:Nhập vào một list số nguyên L, nhập vào số nguyên x, tìm giá trị trong list xa x nhất
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Nhập vào số nguyên x
x = int(input("Nhập số nguyên x: "))

# Tìm giá trị trong list xa x nhất
max_diff = -1  # Khởi tạo khoảng cách lớn nhất
result = None  # Giá trị xa x nhất

for num in L:
    diff = abs(num - x)  # Tính khoảng cách tuyệt đối giữa num và x
    if diff > max_diff:
        max_diff = diff
        result = num

# In ra giá trị xa x nhất
print("Giá trị xa x nhất là:", result)

# BÀI 59:Nhập vào một list số nguyên L, tính giá trị trung bình của list L
# # Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Tính giá trị trung bình của list
if len(L) > 0:
    avg = sum(L) / len(L)
    print("Giá trị trung bình của list là:", avg)
else:
    print("List rỗng, không thể tính giá trị trung bình.")

# BÀI 60: Nhập vào một list số nguyên L, hãy kiểm tra xem L có được sắp xếp từ bé đến lớn hay không, nếu có thì in True, không có thì in False
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Kiểm tra xem list có được sắp xếp từ bé đến lớn hay không
if L == sorted(L):
    print(True)
else:
    print(False)

# BÀI 61 :Nhập vào một list số nguyên L, hãy sắp xếp list L theo thứ tự từ bé đến lớn
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Sắp xếp list theo thứ tự từ bé đến lớn
L.sort()

# In ra list đã được sắp xếp
print("List sau khi sắp xếp là:", L)

# BÀI 62: Nhập vào một list số nguyên L, hãy kiểm tra xem L có phải là một cấp số cộng hay không? Nếu có thì tìm và in ra công sai, nếu không có thì in ra None
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Hàm kiểm tra cấp số cộng và tìm công sai
def is_arithmetic_sequence(seq):
    if len(seq) < 2:
        return None  # Không đủ phần tử để xác định

    common_difference = seq[1] - seq[0]  # Tính công sai ban đầu
    for i in range(2, len(seq)):
        if seq[i] - seq[i - 1] != common_difference:
            return None  # Không phải cấp số cộng

    return common_difference  # Trả về công sai nếu là cấp số cộng

# Kiểm tra và in ra kết quả
common_difference = is_arithmetic_sequence(L)
if common_difference is not None:
    print("List là một cấp số cộng với công sai:", common_difference)
else:
    print(None)

# BÀI 63: Nhập vào một list số nguyên L, Hãy tìm và in ra một vị trí trong L thỏa hai điều kiện: có hai giá trị lân cận và giá trị tại vị trí đó bằng tích hai giá trị lân cận.
# Nếu L không tồn tại giá trị như vậy thì in ra - 1
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Biến để lưu vị trí tìm thấy
position = -1

# Duyệt qua list từ phần tử thứ 1 đến phần tử thứ len(L) - 2
for i in range(1, len(L) - 1):
    if L[i] == L[i - 1] * L[i + 1]:
        position = i
        break  # Ngắt vòng lặp khi tìm thấy

# In ra vị trí thỏa mãn điều kiện hoặc -1 nếu không tìm thấy
print(position)

# BÀI 64:Người ta định nghĩa một list số nguyên là list chẵn lẻ, nếu như tổng 2 phần tử bất kỳ bên trong list đều là số lẻ
# Nhập vào một list số nguyên L và kiểm tra xem L có phải là list chẵn lẻ hay không
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Kiểm tra xem list có phải là list chẵn lẻ hay không
def is_odd_list(seq):
    for num in seq:
        if num % 2 == 0:  # Kiểm tra xem số có phải là số chẵn không
            return False  # Nếu có số chẵn thì không phải list chẵn lẻ
    return True  # Nếu tất cả số đều lẻ

# Gọi hàm kiểm tra và in ra kết quả
if is_odd_list(L):
    print("List là list chẵn lẻ.")
else:
    print("List không phải là list chẵn lẻ.")

# BÀI 65:Người ta định nghĩa một list số nguyên được gọi là “dạng sóng” khi tất cả các phần tử đều lớn hơn hoặc nhỏ hơn hai phần tử xung quanh nó.
# Nhập vào một list số nguyên L và kiểm tra xem L có phải là list “dạng sóng” hay không, nếu có thì ta in ra True, không có thì ta in False
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Hàm kiểm tra list có phải là dạng sóng hay không
def is_wave_form(seq):
    for i in range(1, len(seq) - 1):
        # Kiểm tra điều kiện dạng sóng
        if not ((seq[i] > seq[i - 1] and seq[i] > seq[i + 1]) or (seq[i] < seq[i - 1] and seq[i] < seq[i + 1])):
            return False  # Nếu không thỏa mãn điều kiện, trả về False
    return True  # Nếu tất cả các phần tử đều thỏa mãn điều kiện

# Kiểm tra và in ra kết quả
if is_wave_form(L):
    print(True)
else:
    print(False)

# BÀI 66 : Nhập vào một list số nguyên L, hãy đếm số lượng giá trị trong list thỏa tính chất: “lớn hơn tất cả các giá trị đứng đằng trước nó”
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Biến để đếm số lượng giá trị thỏa mãn
count = 0

# Biến để lưu giá trị lớn nhất đã gặp trước đó
max_value = float('-inf')  # Khởi tạo là âm vô cực

# Duyệt qua từng phần tử trong list
for num in L:
    if num > max_value:
        count += 1  # Tăng số lượng nếu num lớn hơn giá trị lớn nhất trước đó
        max_value = num  # Cập nhật giá trị lớn nhất

# In ra kết quả
print("Số lượng giá trị thỏa tính chất là:", count)

# BÀI 67: Nhập vào một list số nguyên L, hãy đưa các số chẵn trong list về đầu list, số lẻ về cuối list và các phần tử 0 nằm ở giữa
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Khởi tạo các list tạm thời
evens = []  # Danh sách số chẵn
odds = []   # Danh sách số lẻ
zeros = []  # Danh sách số 0

# Duyệt qua từng phần tử trong list
for num in L:
    if num == 0:
        zeros.append(num)  # Thêm số 0 vào danh sách zeros
    elif num % 2 == 0:
        evens.append(num)  # Thêm số chẵn vào danh sách evens
    else:
        odds.append(num)    # Thêm số lẻ vào danh sách odds

# Kết hợp các list lại với nhau
result = evens + zeros + odds

# In ra kết quả
print("List sau khi sắp xếp là:", result)

# BÀI 68 : Nhập vào một list số nguyên L, hãy biến đổi L bằng cách thay đổi vị trí giữa giá trị nhỏ nhất và lớn nhất
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Kiểm tra list không rỗng
if not L:
    print("List rỗng!")
else:
    # Tìm chỉ số của giá trị nhỏ nhất và lớn nhất
    min_index = L.index(min(L))
    max_index = L.index(max(L))

    # Hoán đổi giá trị nhỏ nhất và lớn nhất
    L[min_index], L[max_index] = L[max_index], L[min_index]

    # In ra list đã biến đổi
    print("List sau khi hoán đổi:", L)

# BÀI 69 :Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy tìm và in ra chuỗi có độ dài lớn nhất và số nguyên có giá trị nhỏ nhất
# Nhập vào list có các phần tử bao gồm chuỗi và số nguyên
L = eval(input("Nhập list gồm các phần tử chuỗi và số nguyên (vd: [1, 'abc', 2, 'de', -1]): "))

# Biến để lưu chuỗi có độ dài lớn nhất và số nguyên nhỏ nhất
longest_string = ""
smallest_integer = float('inf')  # Khởi tạo là dương vô cực

# Duyệt qua từng phần tử trong list
for item in L:
    # Kiểm tra nếu phần tử là chuỗi
    if isinstance(item, str):
        if len(item) > len(longest_string):
            longest_string = item  # Cập nhật chuỗi có độ dài lớn nhất
    # Kiểm tra nếu phần tử là số nguyên
    elif isinstance(item, int):
        if item < smallest_integer:
            smallest_integer = item  # Cập nhật số nguyên nhỏ nhất

# In ra kết quả
print("Chuỗi có độ dài lớn nhất:", longest_string)
print("Số nguyên có giá trị nhỏ nhất:", smallest_integer if smallest_integer != float('inf') else "Không có số nguyên")

# BÀI 70 : Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy kiểm tra các phần tử trong L có phải là chuỗi và số xen kẽ nhau không, nếu có thì ta tiến hành tạo một list K mới có các phần tử như sau:
# K[i/2] = L[i]*L[i+1] (với i chẵn)
# Nhập vào list có các phần tử bao gồm chuỗi và số nguyên
L = eval(input("Nhập list gồm các phần tử chuỗi và số nguyên (vd: [1, 'abc', 2, 'de', 3]): "))

# Biến để lưu list mới K
K = []

# Kiểm tra tính xen kẽ
is_alternating = True
for i in range(len(L)):
    if (i % 2 == 0 and not isinstance(L[i], str)) or (i % 2 == 1 and not isinstance(L[i], int)):
        is_alternating = False
        break

# Nếu là xen kẽ, tạo list K
if is_alternating:
    for i in range(0, len(L) - 1, 2):  # Duyệt từ 0 đến len(L) - 1 với bước 2
        # Kiểm tra nếu phần tử i là chuỗi và phần tử i+1 là số nguyên
        if isinstance(L[i], str) and isinstance(L[i + 1], int):
            K.append(L[i] * L[i + 1])  # Tạo phần tử K[i/2] = L[i] * L[i+1]

    # In ra kết quả
    print("List K mới là:", K)
else:
    print("Các phần tử trong list không phải là chuỗi và số xen kẽ nhau.")

# BÀI 71 : Nhập vào một list L có các phần tử là chuỗi (các chuỗi này không có ký tự đặc biệt, dấu câu, ký tự số, chỉ có ký tự chữ cái và khoảng trắng)
# Hãy tìm ra vị trí của chuỗi có nhiều từ nhất
# Nhập vào list các chuỗi
L = eval(input("Nhập list gồm các chuỗi (vd: ['Hello world', 'Python is fun', 'I love programming']): "))

# Biến để lưu vị trí và số từ nhiều nhất
max_words = 0
max_index = -1

# Duyệt qua từng chuỗi trong list
for index, string in enumerate(L):
    word_count = len(string.split())  # Đếm số từ trong chuỗi

    # Kiểm tra nếu số từ trong chuỗi hiện tại lớn hơn số từ lớn nhất đã tìm thấy
    if word_count > max_words:
        max_words = word_count
        max_index = index  # Cập nhật vị trí

# In ra kết quả
if max_index != -1:
    print("Vị trí của chuỗi có nhiều từ nhất là:", max_index)
    print("Chuỗi đó là:", L[max_index])
else:
    print("Không có chuỗi nào trong list.")

# BÀI 72: Nhập vào một list L có các phần tử là chuỗi. Hãy tìm ra chuỗi có vị trí ký tự in hoa lớn nhất
# Nhập vào list các chuỗi
L = eval(input("Nhập list gồm các chuỗi (vd: ['Hello World', 'Python Is Fun', 'Learning Python']): "))

# Biến để lưu chuỗi có ký tự in hoa ở vị trí lớn nhất và chỉ số của nó
max_upper_index = -1
result_string = ""

# Duyệt qua từng chuỗi trong list
for string in L:
    # Duyệt qua từng ký tự trong chuỗi
    for index, char in enumerate(string):
        if char.isupper():  # Kiểm tra nếu ký tự là in hoa
            if index > max_upper_index:  # Kiểm tra vị trí ký tự in hoa
                max_upper_index = index
                result_string = string  # Cập nhật chuỗi có vị trí ký tự in hoa lớn nhất

# In ra kết quả
if result_string:
    print("Chuỗi có ký tự in hoa ở vị trí lớn nhất là:", result_string)
else:
    print("Không có ký tự in hoa trong bất kỳ chuỗi nào.")

# BÀI TẬP XÂY DỰNG HÀM

# BÀI 73: Viết hàm đưa vào 2 số nguyên, số nào lớn hơn thì in bảng cửu chương của số đó
# def print_multiplication_table(a, b):
    # Tìm số lớn hơn
    larger = max(a, b)

    # In bảng cửu chương của số lớn hơn
    print(f"Bảng cửu chương của {larger}:")
    for i in range(1, 11):  # Từ 1 đến 10
        print(f"{larger} x {i} = {larger * i}")

# Nhập vào hai số nguyên
num1 = int(input("Nhập số nguyên thứ nhất: "))
num2 = int(input("Nhập số nguyên thứ hai: "))

# Gọi hàm để in bảng cửu chương
print ("multiplication_table(num1, num2)")

# BÀI 74: Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số nguyên tố hay không
def is_prime(a):
    # Số nhỏ hơn 2 không phải là số nguyên tố
    if a < 2:
        return False
    # Kiểm tra các số từ 2 đến căn bậc hai của a
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

# BÀI 75 :Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số Armstrong hay không
def is_armstrong(a):
    # Chuyển số thành chuỗi để dễ dàng đếm số chữ số và truy cập từng chữ số
    digits = str(a)
    n = len(digits)
    
    # Tính tổng các lũy thừa của từng chữ số lên mũ số lượng chữ số
    sum_of_powers = sum(int(digit) ** n for digit in digits)
    
    # Kiểm tra xem tổng có bằng số ban đầu hay không
    return sum_of_powers == a

# BÀI 76: Viết hàm đưa vào 1 list số nguyên, tìm và trả về vị trí có giá trị lớn nhất trong list

def find_max_index(lst):
    if len(lst) == 0:
        return None  # Trả về None nếu danh sách rỗng

    max_value = lst[0]
    max_index = 0

    # Duyệt qua danh sách, bắt đầu từ vị trí thứ 1
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            max_index = i

    return max_index

# BÀi 77: Viết hàm đưa vào một list số nguyên và một số nguyên dương k.
#  Hãy tìm và trả về vị trí của phần tử đầu tiên có giá trị k trong list số nguyên, nếu không có thì trả về -1
def find_first_occurrence(lst, k):
    # Duyệt qua danh sách
    for index in range(len(lst)):
        if lst[index] == k:
            return index  # Trả về vị trí đầu tiên tìm thấy
    return -1  # Trả về -1 nếu không tìm thấy

# BÀI 78 :Viết hàm đưa vào 1 list có các phần tử là chuỗi, tìm và trả về chuỗi ngắn nhất trong list
def find_shortest_string(lst):
    if len(lst) == 0:
        return None  # Trả về None nếu danh sách rỗng

    shortest_string = lst[0]  # Bắt đầu với chuỗi đầu tiên

    # Duyệt qua danh sách để tìm chuỗi ngắn nhất
    for string in lst:
        if len(string) < len(shortest_string):
            shortest_string = string  # Cập nhật chuỗi ngắn nhất

    return shortest_string

# BÀI 79 :Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tính và trả về giá trị trung bình của a phần tử đầu tiên trong L
def average_of_first_a_elements(L, a):
    # Kiểm tra nếu a lớn hơn số phần tử trong L
    if a > len(L):
        return None  # Trả về None nếu a lớn hơn số phần tử trong L
    
    # Lấy a phần tử đầu tiên
    first_a_elements = L[:a]
    
    # Tính trung bình
    average = sum(first_a_elements) / a
    return average

# BÀI 80: Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a.
#  Hãy tìm và trả về một list mới có số phần tử là a, giá trị các phần tử là các số nguyên tố tìm được trong list L
def is_prime(n):
    """Kiểm tra xem n có phải là số nguyên tố hay không."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_first_a_primes(L, a):
    primes = []  # Danh sách chứa số nguyên tố tìm được
    
    # Duyệt qua từng phần tử trong L
    for number in L:
        if is_prime(number):
            primes.append(number)  # Thêm số nguyên tố vào danh sách
            if len(primes) == a:  # Kiểm tra xem đã đủ a phần tử chưa
                break
    
    return primes  # Trả về danh sách các số nguyên tố
# Bài 81:Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a.
#  Hãy tìm và trả về giá trị lớn thứ a trong list L (nếu a = 1 thì tìm giá trị lớn nhất, a = 2 thì tìm giá trị lớn nhì, a = 3 thì tìm giá trị lớn ba,...)
# C1 
def gia_tri_lon_thu_a(L, a):
    # Bước 1: Sắp xếp danh sách theo thứ tự giảm dần
    L_unique = list(set(L))  # Loại bỏ các giá trị trùng lặp
    L_unique.sort(reverse=True)  # Sắp xếp giảm dần

    # Bước 2: Kiểm tra xem giá trị thứ a có tồn tại không
    if a <= len(L_unique):
        return L_unique[a - 1]  # Trả về giá trị lớn thứ a (a-1 là chỉ số)
    else:
        return None  # Trả về None nếu a lớn hơn số phần tử độc nhất trong L

# Ví dụ sử dụng
L = [3, 1, 4, 4, 2, 5]
a = 2
result = gia_tri_lon_thu_a(L, a)
print(result)  # Kết quả sẽ là 4
# c2:
def gia_tri_lon_thu_a(L, a):
    # Loại bỏ các số trùng lặp bằng cách chuyển sang tập hợp
    unique_values = list(set(L))
    
    # Sắp xếp danh sách theo thứ tự giảm dần
    unique_values.sort(reverse=True)
    
    # Kiểm tra xem a có nằm trong phạm vi số phần tử không
    if a <= len(unique_values):
        return unique_values[a - 1]  # Trả về giá trị lớn thứ a
    else:
        return None  # Trả về None nếu không có giá trị lớn thứ a

# Ví dụ sử dụng
L = [3, 1, 4, 4, 5, 5, 2]
a = 2
print(gia_tri_lon_thu_a(L, a))  # Kết quả sẽ là 4

# BÀI TẬP XỬ LÝ DICTIONARY

# Bài 82: Viết hàm đưa vào 1 dictionary có các phần tử có giá trị là số nguyên, tìm và trả về key có giá trị lớn nhất
def key_max_value(d):
    if not d:
        return None  # Trả về None nếu dictionary rỗng

    # Tìm key có giá trị lớn nhất
    max_key = max(d, key=d.get)  # Sử dụng hàm max với tham số key để tìm key tương ứng
    return max_key

# Ví dụ sử dụng
d = {'a': 10, 'b': 20, 'c': 15}
result = key_max_value(d)
print(result)  # Kết quả sẽ là 'b'

# Bài 83: Viết hàm đưa vào 1 dictionary có các phần tử có key là chuỗi, tìm và trả về giá trị của key có độ dài lớn nhất
def key_max_value(d):
    if not d:
        return None  # Trả về None nếu dictionary rỗng

    # Tìm key có giá trị lớn nhất
    max_key = max(d, key=d.get)  # Sử dụng hàm max với tham số key để tìm key tương ứng
    return max_key

# Ví dụ sử dụng
d = {'a': 10, 'b': 20, 'c': 15}
result = key_max_value(d)
print(result)  # Kết quả sẽ là 'b'

# Bài 84 :Viết hàm có tham số đầu vào là một list L có các phần tử là chuỗi. Hãy tạo ra một dictionary D mã hóa, với mỗi một phần tử trong L được mã hóa thành một con số (theo thứ tự từ 0 tăng dần lên 1 đơn vị). Sau đó trả về list đã được mã hóa
# Ví dụ:
# Cho
# L = ["đen","vàng","xanh","vàng","xanh","đỏ","hồng"]
# Xây dựng dictionary mã hóa:
# D = {'đen':0,'vàng':1,'xanh':2,'đỏ':3,'hồng':4}
# Trả về List mã hóa:
# L_mahoa = [0, 1, 2, 1, 2, 3, 4]
def ma_hoa_list(L):
    D = {}  # Tạo dictionary mã hóa
    L_mahoa = []  # Danh sách mã hóa

    # Bước 1: Tạo dictionary mã hóa
    for item in L:
        if item not in D:
            D[item] = len(D)  # Gán mã cho phần tử mới
        L_mahoa.append(D[item])  # Thêm giá trị mã hóa vào danh sách kết quả

    return L_mahoa, D  # Trả về danh sách mã hóa và dictionary

# Ví dụ sử dụng
L = ["đen", "vàng", "xanh", "vàng", "xanh", "đỏ", "hồng"]
L_mahoa, D = ma_hoa_list(L)
print("List mã hóa:", L_mahoa)  # Kết quả sẽ là [0, 1, 2, 1, 2, 3, 4]
print("Dictionary mã hóa:", D)   # Kết quả sẽ là {'đen': 0, 'vàng': 1, 'xanh': 2, 'đỏ': 3, 'hồng': 4}

# Bài 85:Viết hàm có tham số đầu vào là một dictionary, hãy tạo một dictionary mới hoán đổi giá trị và key của dictionary đầu vào, rồi trả về dicionary mới đó.
#  Nếu sau khi hoán đổi có 2 key trùng nhau (do dictionary đầu vào có 2 giá trị trùng nhau), hàm trả về None
def hoan_doi_dict(d):
    d_hoan_doi = {}  # Tạo dictionary mới để hoán đổi

    for key, value in d.items():
        # Kiểm tra xem value đã tồn tại trong dictionary mới chưa
        if value in d_hoan_doi:
            return None  # Nếu trùng, trả về None
        d_hoan_doi[value] = key  # Hoán đổi key và value

    return d_hoan_doi  # Trả về dictionary mới

# Ví dụ sử dụng
d = {'a': 1, 'b': 2, 'c': 3}
d_hoan_doi = hoan_doi_dict(d)
print(d_hoan_doi)  # Kết quả sẽ là {1: 'a', 2: 'b', 3: 'c'}

d2 = {'a': 1, 'b': 2, 'c': 1}
d_hoan_doi2 = hoan_doi_dict(d2)
print(d_hoan_doi2)  # Kết quả sẽ là None (do có giá trị trùng nhau)

# BÀI TẬP LUYỆN TẬP & ỨNG DỤNG
# Bài 86: Một nhà hàng có các món ăn: Gà rán, hamburger, cocacola
# Giá của gà rán là: 30.000đ
# Giá của hamburger là: 25.000đ
# Giá của cocacola là: 10.000đ
# Yêu cầu người dùng nhập vào số lượng từng món ăn.
# Sau đó in ra hóa đơn theo dạng như sau:
# Chào mừng các bạn đến với nhà hàng thức ăn nhanh!
# Mời bạn nhập số lượng từng món ăn:
# Gà rán: 2
# Hamburger: 3
# Cocacola: 5
# Hóa đơn:
# Gà rán             30.000đ x 2
# Hamburger          25.000đ x 3
# Cocacola           10.000đ x 5
# Tổng:
# Gà rán             60.000đ
# Hamburger          75.000đ
# Cocacola           50.000đ
# Tổng trước thuế    185.000đ
# Thuế(5%)           9.250đ
# Tổng sau thuế      194.250đ
# Phần bên trái có số ký tự là 20 ký tự

def in_hoa_don():
    # Giá của các món ăn
    menu = {
        'Gà rán': 30000,
        'Hamburger': 25000,
        'Cocacola': 10000
    }

    # Yêu cầu người dùng nhập số lượng từng món ăn
    print("Chào mừng các bạn đến với nhà hàng thức ăn nhanh!")
    print("Mời bạn nhập số lượng từng món ăn:")
    so_luong_ga_ran = int(input("Gà rán: "))
    so_luong_hamburger = int(input("Hamburger: "))
    so_luong_cocacola = int(input("Cocacola: "))

    # Tính tổng tiền từng món
    tong_ga_ran = menu['Gà rán'] * so_luong_ga_ran
    tong_hamburger = menu['Hamburger'] * so_luong_hamburger
    tong_cocacola = menu['Cocacola'] * so_luong_cocacola

    # Tổng trước thuế
    tong_truoc_thue = tong_ga_ran + tong_hamburger + tong_cocacola

    # Tính thuế (5%)
    thue = tong_truoc_thue * 0.05
    # Tổng sau thuế
    tong_sau_thue = tong_truoc_thue + thue
    # In hóa đơn
    print("\nHóa đơn:")
    print(f"{'Gà rán':<20}{menu['Gà rán']:>6,}đ x {so_luong_ga_ran}")
    print(f"{'Hamburger':<20}{menu['Hamburger']:>6,}đ x {so_luong_hamburger}")
    print(f"{'Cocacola':<20}{menu['Cocacola']:>6,}đ x {so_luong_cocacola}")
    print("\nTổng:")
    print(f"{'Gà rán':<20}{tong_ga_ran:>6,}đ")
    print(f"{'Hamburger':<20}{tong_hamburger:>6,}đ")
    print(f"{'Cocacola':<20}{tong_cocacola:>6,}đ")
    print(f"{'Tổng trước thuế':<20}{tong_truoc_thue:>6,}đ")
    print(f"{'Thuế(5%)':<20}{thue:>6,.0f}đ")
    print(f"{'Tổng sau thuế':<20}{tong_sau_thue:>6,.0f}đ")
# Gọi hàm để in hóa đơn
in_hoa_don()
# Bài 87:Viết hàm cho giá trị đầu vào là list số nguyên dương L và số nguyên dương k.
#  Hãy tạo và trả về một list L_kq có các phần tử là giá trị của phần tử xuất hiện nhiều hơn k lần trong list L theo thứ tự tăng dần
def tim_phan_tu_xuat_hien_hon_k(L, k):
    # Bước 1: Tạo dictionary đếm số lần xuất hiện của từng phần tử
    dem = {}
    for num in L:
        if num in dem:
            dem[num] += 1
        else:
            dem[num] = 1

    # Bước 2: Tìm các phần tử xuất hiện nhiều hơn k lần
    L_kq = [num for num, count in dem.items() if count > k]

    # Bước 3: Sắp xếp danh sách kết quả theo thứ tự tăng dần
    L_kq.sort()

    return L_kq
# Ví dụ sử dụng
L = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
k = 2
L_kq = tim_phan_tu_xuat_hien_hon_k(L, k)
print(L_kq)  # Kết quả sẽ là [3, 4]
# Bài 88: Viết hàm cho giá trị đầu vào là list số nguyên dương L và số nguyên dương k. 
# Tìm và trả về đoạn list dài nhất trong L có giá trị trung bình là k
def tim_doan_list_trung_binh_k(L, k):
    n = len(L)  # Số phần tử trong danh sách L
    max_len = 0  # Độ dài lớn nhất của đoạn tìm thấy
    longest_sublist = []  # Đoạn dài nhất tìm thấy

    # Duyệt qua tất cả các đoạn con trong L
    for i in range(n):
        for j in range(i, n):
            sublist = L[i:j+1]  # Lấy đoạn từ i đến j
            avg = sum(sublist) / len(sublist)  # Tính trung bình của đoạn con

            # Kiểm tra xem giá trị trung bình có bằng k không
            if avg == k:
                if len(sublist) > max_len:  # Nếu độ dài đoạn con này lớn hơn đoạn dài nhất trước đó
                    max_len = len(sublist)
                    longest_sublist = sublist

    return longest_sublist
# Ví dụ sử dụng
L = [1, 2, 3, 4, 5, 6, 7]
k = 4
longest_sublist = tim_doan_list_trung_binh_k(L, k)
print(longest_sublist)  # Kết quả sẽ là [3, 4, 5]

# Bài 89: Một người dùng số tiền là U đô-la và V Euro để mua một loại nguyên liệu sản xuất.

# Có N công ty nước ngoài bán nguyên liệu trên được đánh số từ 1 đến N. Công ty thứ i có giá bán Ai đô la/1 kg nguyên liệu và Bi Euro/1 kg nguyên liệu.

# Tuy nhiên, tại mỗi công ty chỉ bán nguyên liệu cho một khách hàng hoặc theo đô-la, hoặc theo Euro.

# Hãy giúp người đó tìm cách chọn ra 2 công ty để mua hàng sao cho số lượng nguyên liệu sản xuất có thể mua được là nhiều nhất.

# Nhập vào: U, V và List A và List B

# In ra: Số lượng nguyên liệu S (kg) người đó mua được với 2 chữ số thập phân.
def so_luong_nguyen_lieu(U, V, A, B):
    N = len(A)  # Số lượng công ty
    
    max_nguyen_lieu = 0.0  # Lượng nguyên liệu lớn nhất

    # Duyệt qua tất cả các cặp công ty i và j (i != j)
    for i in range(N):
        for j in range(N):
            if i != j:  # Chỉ xét khi i và j là hai công ty khác nhau
                # Tính lượng nguyên liệu có thể mua từ công ty i (bằng đô-la) và công ty j (bằng Euro)
                so_luong = (U / A[i]) + (V / B[j])
                
                # Cập nhật số lượng nguyên liệu lớn nhất nếu tìm thấy giá trị lớn hơn
                if so_luong > max_nguyen_lieu:
                    max_nguyen_lieu = so_luong
    return round(max_nguyen_lieu, 2)  # Trả về số lượng với 2 chữ số thập phân
# Ví dụ sử dụng:
U = 1000  # Số tiền đô-la
V = 800   # Số tiền Euro
A = [50, 60, 70]  # Giá bán đô-la/kg của các công ty
B = [40, 30, 50]  # Giá bán Euro/kg của các công ty
ket_qua = so_luong_nguyen_lieu(U, V, A, B)
print(ket_qua)  # Kết quả sẽ là số lượng nguyên liệu lớn nhất với 2 chữ số thập phân
# Bài 90: Phỏng đoán COLLATZ
# Giả sử ta có một số n
# Phỏng đoán COLLATZ hoạt động như sau:
# Nếu n là số chẵn, thì ta chia n cho 2 (n/2)
# Nếu n là số lẻ, thì ta nhân n cho 3 rồi + 1 (3n + 1)
# Phỏng đoán hoạt động cho đến khi nào n = 1
# Yêu cầu:
# Nhập vào số nguyên dương m, hãy in ra dãy phỏng đoán COLLATZ từ 1 đến m (mỗi một phỏng đoán ta in trên 1 dòng, mỗi một số cách nhau một dấu phẩy)
# Ví dụ:
# Nhập: m = 6
# In ra:

# 1 2,1 3,10,5,16,8,4,2,1 4,2,1 5,16,8,4,2,1 6,3,10,5,16,8,4,2,1 
def collatz(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:  # Nếu n là số chẵn
            n = n // 2
        else:  # Nếu n là số lẻ
            n = 3 * n + 1
    sequence.append(1)  # Thêm số 1 vào cuối dãy
    return sequence

def in_day_collatz(m):
    for i in range(1, m + 1):
        # Gọi hàm collatz để lấy dãy cho từng số từ 1 đến m
        sequence = collatz(i)
        # In ra dãy số cách nhau bởi dấu phẩy
        print(",".join(map(str, sequence)))

# Ví dụ sử dụng:
m = int(input("Nhập m: "))
in_day_collatz(m)

# Bài 91:Một khách sạn có N phòng đôi được đánh số từ 1 đến N và M đoàn khách.
# Với mỗi đoàn khách, ta xếp mỗi cặp khách của đoàn vào một phòng trống theo thứ tự phòng tăng dần.
# Nếu đoàn khách có số người lẻ thì người khách cuối cùng được xếp vào một phòng trống tiếp theo.
# Nếu đã hết phòng còn trống thì ta sẽ xếp khách vào những phòng mới chỉ có 1 khách theo thứ tự phòng tăng dần.
# In ra số khách của mỗi phòng sau khi xếp.
# Giả sử không có 2 đoàn khách nào đến cùng một lúc.
# Ví dụ 1:
N = 7, M = 3
doankhach = [3,7,3]
# Ta in: 2, 2, 2, 2, 2, 1, 2
# Ví dụ 2:
N = 5, M = 3
doankhach = [2,3,2]
# Ta in: 2, 2, 1, 2, 0
def xep_khach_san(N, M, doankhach):
    # Bước 1: Khởi tạo danh sách số lượng khách trong mỗi phòng
    phong = [0] * N  # Ban đầu tất cả các phòng đều trống
    
    index = 0  # Biến để theo dõi phòng hiện tại

    # Bước 2: Xếp khách cho từng đoàn
    for so_khach in doankhach:
        while so_khach > 0:
            # Nếu phòng hiện tại còn trống (phong[index] < 2)
            if phong[index] < 2:
                # Số khách xếp vào phòng này (tối đa 2 - phong[index])
                xep_vao_phong = min(so_khach, 2 - phong[index])
                phong[index] += xep_vao_phong
                so_khach -= xep_vao_phong
            
            # Chuyển sang phòng tiếp theo
            index += 1
            if index == N:
                index = 0  # Quay lại phòng đầu tiên nếu hết phòng
            
    # Bước 3: In kết quả
    print(",".join(map(str, phong)))

# Ví dụ 1:
N = 7
M = 3
doankhach = [3, 7, 3]
xep_khach_san(N, M, doankhach)  # Output: 2,2,2,2,2,1,2

# Ví dụ 2:
N = 5
M = 3
doankhach = [2, 3, 2]
xep_khach_san(N, M, doankhach)  # Output: 2,2,1,2,0

# BÀI TẬP XỬ LÝ ĐỌC GHI FILE
# Bài 92:File 2to10.inp là file chứa các số nhị phân (mỗi dòng 1 số), hãy chuyển các số nhị phân đó sang số thập phân rồi lưu lại vào file 2to10.out (mỗi dòng 1 số)
# VD
# 2to10.inp
# 2to10.out
# 0011
# 111110000011111
# 1001010100000010111110001111111111	3
# 31775
# 9999999999
def binary_to_decimal(input_file, output_file):
    with open(input_file, 'r') as inp, open(output_file, 'w') as out:
        # Đọc từng dòng trong file đầu vào
        for line in inp:
            binary_str = line.strip()  # Loại bỏ các ký tự trắng (nếu có)
            
            try:
                # Chuyển từ nhị phân sang thập phân
                decimal_number = int(binary_str, 2)
                # Ghi kết quả vào file đầu ra
                out.write(str(decimal_number) + '\n')
            except ValueError:
                # Nếu không phải là số nhị phân hợp lệ thì ghi "INVALID"
                out.write("INVALID\n")

# Sử dụng hàm với file cụ thể
binary_to_decimal('2to10.inp', '2to10.out')

# Bài 93:Hãy phân tích một số tự nhiên thành các thừa số nguyên tố
# File thuaso.inp:
# - Chứa các số tự nhiên lớn hơn 1(mỗi số cách nhau một dòng)
# File thuaso.out:
# - Kết quả phân tích từng số trong file thuaso.inp, 
# mỗi một dòng tương ứng với kết quả tách được được từ trong file thuaso.inp, các thừa số cách nhau bằng một khoảng trắng
# VD:
# thuaso.inp	thuaso.out
# 2
# 8
# 10
# 15
# 100
# 101
# 10250	2
# 2 2 2
# 2 5
# 3 5
# 2 2 5 5
# 101
# 2 5 5 5 41
def phan_tich_thua_so(n):
    i = 2
    thua_so = []
    # Phân tích số n thành thừa số nguyên tố
    while i * i <= n:  # Kiểm tra các thừa số từ 2 đến sqrt(n)
        while n % i == 0:  # Nếu n chia hết cho i
            thua_so.append(i)
            n //= i  # Chia n cho i
        i += 1
    if n > 1:  # Số còn lại là thừa số nguyên tố cuối cùng
        thua_so.append(n)
    return thua_so

def xu_ly_file(input_file, output_file):
    with open(input_file, 'r') as inp, open(output_file, 'w') as out:
        # Đọc từng dòng trong file đầu vào
        for line in inp:
            number = int(line.strip())  # Lấy số tự nhiên từ file
            thua_so = phan_tich_thua_so(number)  # Phân tích thành thừa số
            # Ghi kết quả vào file, các thừa số cách nhau bằng khoảng trắng
            out.write(" ".join(map(str, thua_so)) + "\n")

# Sử dụng hàm với file thuaso.inp và thuaso.out
xu_ly_file('thuaso.inp', 'thuaso.out')

# Bài 94: Cho một chuỗi ký tự S (gồm chữ và số). Hãy viết chương trình tách chữ và số thành hai chuỗi riêng biệt.
# File chuoi.inp chứa duy nhất 1 chuỗi S

# Hãy tách và ghi vào file chuoi.out 2 dòng, dòng thứ nhất ghi chuỗi ký tự chữ, dòng thứ hai ghi chuỗi ký tự số.

# Nếu như chuỗi nào rỗng thì ghi dấu trừ ‘-’.
# VD1:
# chuoi.inp	chuoi.out
# a1B2c34d	aBcd
# 1234
# VD2:
# chuoi.inp	chuoi.out
# abghcGGG	abghcGGG
def tach_chu_so(input_file, output_file):
    with open(input_file, 'r') as inp, open(output_file, 'w') as out:
        chuoi = inp.read().strip()  # Đọc chuỗi S từ file và loại bỏ ký tự trắng thừa
        
        chuoi_chu = ""
        chuoi_so = ""

        # Duyệt qua từng ký tự trong chuỗi
        for ky_tu in chuoi:
            if ky_tu.isalpha():  # Nếu là chữ cái
                chuoi_chu += ky_tu
            elif ky_tu.isdigit():  # Nếu là chữ số
                chuoi_so += ky_tu

        # Nếu chuỗi nào rỗng, thay bằng dấu '-'
        if not chuoi_chu:
            chuoi_chu = "-"
        if not chuoi_so:
            chuoi_so = "-"
        
        # Ghi kết quả vào file, mỗi chuỗi trên một dòng
        out.write(chuoi_chu + "\n")
        out.write(chuoi_so + "\n")

# Sử dụng hàm với file cụ thể
tach_chu_so('chuoi.inp', 'chuoi.out')

# Bài 95:Cho một dãy số 1, 1, 1, 2, 3, 4, 6,... (quy luật a[i] = a[i - 1] + a[i - 3])
# Với a[1] = 1, a[2] = 1, a[3] = 1 (3 số đầu tiên)
# File dayso.inp chứa các số nguyên k (k < 1000), mỗi dòng 1 số
# Hãy tìm a[k] trong dãy số và ghi vào file dayso.out
# VD:
# dayso.inp	
# dayso.out
# 3
# 10
# 50
# 101	1
# 19
# 83316385
# 24382819596721629
def tinh_day_so(max_k):
    # Khởi tạo dãy với 3 phần tử đầu là 1
    a = [0] * (max_k + 1)
    a[1] = a[2] = a[3] = 1
    
    # Tính toán các giá trị tiếp theo dựa trên công thức
    for i in range(4, max_k + 1):
        a[i] = a[i - 1] + a[i - 3]
    
    return a

def xu_ly_file(input_file, output_file):
    # Đọc các số k từ file đầu vào
    with open(input_file, 'r') as inp:
        k_list = [int(line.strip()) for line in inp.readlines()]
    
    # Tìm giá trị lớn nhất của k trong file để tính đến giá trị đó
    max_k = max(k_list)
    
    # Tính dãy số đến giá trị max_k
    day_so = tinh_day_so(max_k)
    
    # Ghi kết quả tương ứng của từng k vào file đầu ra
    with open(output_file, 'w') as out:
        for k in k_list:
            out.write(str(day_so[k]) + '\n')

# Sử dụng hàm với file cụ thể
xu_ly_file('dayso.inp', 'dayso.out')

# Bài 96: Hai số được coi là bạn của nhau khi tổng các ước số (ngoại trừ chính nó) của số này bằng số kia và ngược lại, cụ thể:
#  tổng ước số của M = N và tổng ước số của N = M thì M và N là bạn
# Trong file soban.inp là số K, hãy liệt kê các cặp số M N (với 1 ≤ M < N ≤ K) và ghi vào file soban.out (mỗi cặp một dòng)
# VD:
# soban.inp	soban.out
# 3000	220 284
# 1184 1210
# 2620 2924
def tong_uoc_so(n):
    total = 0
    # Tính tổng các ước số của n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:  # Nếu i là ước số của n
            total += i
            if i != n // i and i != 1:  # Thêm ước số đối
                total += n // i
    return total

def tim_cac_cap_ban(input_file, output_file):
    with open(input_file, 'r') as inp:
        K = int(inp.read().strip())  # Đọc số K từ file
        
    cap_ban = []  # Danh sách lưu các cặp bạn
    
    # Tạo danh sách để lưu tổng các ước số cho từng số
    tong_uoc = [0] * (K + 1)
    
    # Tính tổng ước số cho từng số từ 1 đến K
    for n in range(1, K + 1):
        tong_uoc[n] = tong_uoc_so(n)
    
    # Tìm các cặp bạn
    for M in range(1, K):
        N = tong_uoc[M]  # Tìm N là tổng ước số của M
        if M < N <= K and tong_uoc[N] == M:  # Kiểm tra điều kiện bạn
            cap_ban.append((M, N))
    
    # Ghi kết quả vào file
    with open(output_file, 'w') as out:
        for M, N in cap_ban:
            out.write(f"{M} {N}\n")

# Sử dụng hàm với file cụ thể
tim_cac_cap_ban('soban.inp', 'soban.out')

# Bài 97: Cho N (N ≤ 100) điểm trên hệ trục tọa độ Oxy, hãy đếm xem có bao nhiêu tam giác cân được tạo thành từ các điểm đó.
# File tgcan.inp:
# - Dòng đầu tiên trong file chứa số N
# - N dòng tiếp theo chứa các cặp tọa độ các điểm (mỗi dòng một cặp, mỗi số cách nhau một khoảng trắng)
# Ghi vào file tgcan.out số lượng tam giác cân tạo được
# VD:
# tgcan.inp	tgcan.out
# 4
# 0 0
# 1 0
# 2 0
# 1 1
# 3
def khoang_cach_binh_phuong(p1, p2):
    # Tính bình phương khoảng cách giữa hai điểm p1 và p2
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def dem_tam_giac_can(input_file, output_file):
    with open(input_file, 'r') as inp:
        N = int(inp.readline().strip())  # Đọc số điểm N
        points = [tuple(map(int, inp.readline().strip().split())) for _ in range(N)]  # Đọc tọa độ các điểm

    count = 0  # Đếm số lượng tam giác cân

    # Kiểm tra tất cả các bộ ba điểm để xác định tam giác cân
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                # Tính bình phương khoảng cách giữa các cặp điểm
                d1 = khoang_cach_binh_phuong(points[i], points[j])
                d2 = khoang_cach_binh_phuong(points[j], points[k])
                d3 = khoang_cach_binh_phuong(points[i], points[k])
                
                # Kiểm tra xem có cặp cạnh nào bằng nhau
                if d1 == d2 or d1 == d3 or d2 == d3:
                    count += 1  # Nếu có, tăng số lượng tam giác cân

    # Ghi kết quả vào file
    with open(output_file, 'w') as out:
        out.write(str(count) + '\n')

# Sử dụng hàm với file cụ thể
# dem_tam_giac_can('tgcan.inp', 'tgcan.out')

# Bài 98:Một doanh nhân, sau khi thực hiện mua bán N (N ≤ 100) chuyến hàng, mỗi chuyến hàng có tổng giá trị mua M và tổng giá trị bán B (M, B có thể lên đến 20 chữ số) mới tính xem mình huề vốn, lời hay lỗ, bao nhiêu tiền. Hãy viết chương trình để giúp doanh nhân trên tính toán kết quả kinh doanh.
# File kinhdoanh.inp:
# - Dòng đầu tiên trong file chứa số N
# - N dòng tiếp theo, mỗi dòng chứa cặp số M và B, hai số này cách nhau một khoảng trắng
# Ghi ra file kinhdoanh.out số tiền lời (nếu lỗ in ra số âm)
# VD:
# kinhdoanh.inp	kinhdoanh.out
# 5
# 50 65
# 150 141
# 15 30
# 121 200
# 300 300	100
def tinh_ket_qua_kinh_doanh(input_file, output_file):
    with open(input_file, 'r') as inp:
        N = int(inp.readline().strip())  # Đọc số chuyến hàng N
        tong_mua = 0  # Khởi tạo tổng giá trị mua
        tong_ban = 0  # Khởi tạo tổng giá trị bán
        
        # Đọc từng cặp M và B và tính tổng
        for _ in range(N):
            M, B = map(int, inp.readline().strip().split())
            tong_mua += M
            tong_ban += B

    # Tính lợi nhuận
    loi_nhuan = tong_ban - tong_mua

    # Ghi kết quả vào file
    with open(output_file, 'w') as out:
        out.write(str(loi_nhuan) + '\n')

# Sử dụng hàm với file cụ thể
tinh_ket_qua_kinh_doanh('kinhdoanh.inp', 'kinhdoanh.out')

# Bài 99: Từ chuỗi ngày/tháng/năm theo cấu trúc dd/mm/yyyy và số N (N ≤ 1000) cho trước. Hãy cho biết ngày/tháng/năm (dd/mm/yyyy) sau N ngày.
# File ngay.inp:
# - Chứa ngày/tháng/năm và số N
# File ngay.out:
# - Chứa kết quả là ngày/tháng/năm sau N ngày

# VD:

# ngay.inp	ngay.out
# 15/03/2017 100	23/06/2017
from datetime import datetime, timedelta

def tinh_ngay_sau_N(input_file, output_file):
    with open(input_file, 'r') as inp:
        # Đọc dòng đầu tiên và tách ngày tháng năm và N
        line = inp.readline().strip()
        date_str, N_str = line.split()
        N = int(N_str)  # Chuyển đổi N thành số nguyên

        # Chuyển đổi chuỗi ngày tháng năm thành đối tượng datetime
        start_date = datetime.strptime(date_str, '%d/%m/%Y')

        # Tính ngày sau N ngày
        new_date = start_date + timedelta(days=N)

        # Chuyển đổi đối tượng datetime về định dạng dd/mm/yyyy
        result_date_str = new_date.strftime('%d/%m/%Y')

    # Ghi kết quả vào file
    with open(output_file, 'w') as out:
        out.write(result_date_str + '\n')

# Sử dụng hàm với file cụ thể
tinh_ngay_sau_N('ngay.inp', 'ngay.out')

# Bài 100: Cho trước số tự nhiên N. Hãy viết chương trình cho biết N có thể biểu diễn thành tổng của hai hoặc nhiều số tự nhiên liên tiếp hay không? Nếu có, thì bao nhiêu cách và hãy liệt kê tất cả các cách có thể có. Nếu không, thì thông báo bằng số 0.
# File bieudienso.inp:
# - Chứa N
# File bieudienso.out:
# - Chứa các trường hợp có thể tách được, mỗi số cách nhau một dấu cộng, mỗi dòng một trường hợp
# VD:

# bieudienso.inp	bieudienso.out
# 9	2
# 4+5
# 2+3+4
def bieudienso(input_file, output_file):
    with open(input_file, 'r') as inp:
        N = int(inp.readline().strip())
    
    results = []
    count = 0
    
    # Duyệt từ k = 2 đến một giá trị k hợp lệ
    for k in range(2, N):
        # Tính tổng k(k-1)/2
        sum_k_minus_1 = k * (k - 1) // 2
        
        if sum_k_minus_1 >= N:
            break
        
        if (N - sum_k_minus_1) % k == 0:
            a = (N - sum_k_minus_1) // k
            if a > 0:  # a phải là số tự nhiên
                count += 1
                sequence = '+'.join(str(a + i) for i in range(k))
                results.append(sequence)

    # Ghi kết quả vào file
    with open(output_file, 'w') as out:
        if count == 0:
            out.write('0\n')
        else:
            out.write(f'{count}\n')
            out.write('\n'.join(results) + '\n')

# Sử dụng hàm với file cụ thể
bieudienso('bieudienso.inp', 'bieudienso.out')
