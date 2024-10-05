# BÀI TẬP NHẬP LIỆU VÀ TOÁN TỬ CƠ BẢN
# BÀI 1: Nhập vào số n, hãy nhân n lên cho 3, rồi cộng 1 sau đó in kết quả ra màn hình
# a=int(input("nhập vào số nguyên a: "))
# n=(a*3)+1
# print("khi a nhân cho ba và cộng cho một là: ",n)
# BÀI 2: Nhập vào số n, hãy mũ 2 rồi chia cho 3, sau đó in kết quả ra màn hình
# a=int(input("nhập vào số nguyên a: "))
# n=(a**2)/3
# print("số in ra màng hình là: ",n)
# BÀI 3:Nhập vào nhiệt độ c, in ra nhiệt độ F
# a=float(input("nhập vào nhiệt độ c: "))
# n=(a*1.8)+32
# print("nhiệt độ f là: ",n)
# BÀI 4:Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False
# a=int(input("nhập vào số nguyên a: "))
# if a%2==0:
#     print("TRUE")
# else:
#     print("FALSE")
# BÀI 5:  Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
# cách 1:
# a=int(input("nhập số nguyên a: "))
# if a %3 == 0 and 50<= a <=100:
#     print("TRUE")
# else:
#     print("FALSE")
# cách 2:
# a=int(input("nhập vào số nguyên a: "))
# print(a%3==0 and 50<=a<=100)
# BÀI 6: Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
# CÁCH 1: 
# a=int(input("nhập vào số nguyên a: "))
# if a%5==0 and not 20<=a<=70:
#     print("TRUE")
# else:

#     print("FALSE")
# # CÁCH 2:
# a=int(input("nhập vào số nguyên a: "))
# print(a%5==0 and not 20<=a<=70)
# BÀI 7: Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
# a=int(input("nhập vào số nguyên a: "))
# b=int(input("nhập vào số nguyên b: "))
# print(a%2==0 or b%2==0 )
# # cách 2:
# a=int(input("nhập vào số nguyên a: "))
# b=int(input("nhập vào số nguyên b: "))
# if a%2==0 or b%2==0: 
#     print("TRUE")
# else:
#     print("FALSE")
# BÀI 8: Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False
# a=float(input("nhập vào một số a: "))
# b=round(a)
# print(a==b )
# BÀI 9:Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False
# a=int(input("nhập số nguyên a:  "))
# cana=a**0.5
# print(cana==round(cana))
# BÀI 10:Nhập vào lương tháng này nhận được, ta phải đưa cho vợ 90% số tiền lương đó. Hãy in ra lương ta giữ lại
# a=int(input("nhập vào lương tháng này bạn nhận được: "))
# print("lương giữ lại còn: ",a*0.1)
# BÀI 11:Nhập vào 3 số a, b, c. In ra kết quả là tổng của ba số đó
# a=int(input("nhập vào số nguyên a: "))
# b=int(input("nhập vào số nguyên b: "))
# c=int(input("nhập vào số nguyên c: "))
# tong=a+b+c
# print("tổng ba số a,b,a là: ",tong)
# BÀI 12: Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c
# Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
# a=int(input("nhập vào số nguyên a: "))
# b=int(input("nhập vào số nguyên b: "))
# c=int(input("nhập vào số nguyên c: "))
# d=(a+b)**c 
# print(d)
# if 100<=d<=200:
#     print("TRUE")
# else:
#     print("FALSE")
# BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN
# BÀI 13:Nhập vào số nguyên dương a, nếu a lớn hơn 10 thì ta in ra đây là số lớn hơn 10
# a=int(input("nhập vào số nguyên a: "))
# if a>10 :
#     print("đây là số lớn hơn 10: ")
# else:
#     print("đây là số nhỏ hơn 10: ")
# BÀI 14: Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ
# a=int(input("nhập vào số nguyên dương a: "))
# print("số này đặc biệt: ")
# if a%2==0:
#     print("đây là số chẵn ")
# else:
#     print("đây là số lẻ: ")
# BÀI 15 và 16 :))) :Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không
# a=int(input("nhập vào số nguyên a: "))
# b=int(input("nhập vào số nguyên b: "))
# c=int(input("nhập vào số nguyên c: "))
# if (a+b>c and b+c>a and a+c>b):
#     if a==b==c :
#         print("đây là tam giác điều: ")
#     elif  a==b or a==c or b==c: 
#         if a**2+b**2 == c**2 or a**2+c**2 == b**2 or c**2+b**2 == a**2 :
#             print("đây là tam giác vuông cân: ")
#         else:
#             print("đây là tam giác cân: ")
#     elif a**2+b**2 == c**2 or a**2+c**2 == b**2 or c**2+b**2 == a**2 :
#         print("đây là tam giác vuông: ")
#     else:
#         print("đây là tam giác thường: ")
# else:
#     print("đây không cấu tạo thành tam giác: ")
# BÀI 17: Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại
# a=int(input("nhập vào số nguyên a: "))
# b=int(input("nhập vào số nguyên b: "))
# c=int(input("nhập vào số nguyên c: "))
# if a>b:
#     a,b=b,a
# if a>c:
#     a,c=c,a
# if b>c:
#     b,c=c,b
# print(a,b,c)
# BÀI 18: Giải và biện luận phương trình ax + b = 0
# a=int(input("nhập vào số nguyên a: "))
# b=int(input("nhập vào số nguyên b: "))
# print ("phương trình"+str(a)+"x+"+str(b)+"=0" )
# if a==0:
#     if b==0:
#         print("phương trình vô số nghiệm: ")
#     else:
#         print("phương trình vô nghiệm: ")
# else:
#     print("nghiệm của phương trình là: ",-b/a)        
# BÀI 19: Giải và biện luận phương trình ax^2 + bx + c = 0
# a=int(input("nhập vào số nguyên a: "))
# b=int(input("nhập vào số nguyên b: "))
# c=int(input("nhập vào số nguyên c: "))
# print("phương trình"+ str(a) +"x^2 + " + str(b)+"x+"+ str(c)+ "=0")
# if a==0:
#     if b==0:
#         if c==0:
#             print("phương trình vô số nghiệm: ")
#         else:
#             print("phương trình vô nghiệm: ")
#     else: 
#         print("phương trình có một nghiệm là:",-c/b)
# else:
#     denta = b**2 - 4*a*c
#     if denta>0:
#         candenta= denta**0.5
#         x1= (-b +candenta)/(2*a)
#         x2= (-b -candenta)/(2*a)
#         print("phương trình này có hai nghiệm phân biệt là: ",x1, "và" ,x2)
#     elif denta==0:
#         print("phương trình có nghiệm kép x1=x2:  ",-b/(a*a))
#     else:
#         print("phương trình vô nghiệm: ")
# BÀI 20 :Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày
# a=int(input("nhập vào tháng mà bạn muốn tìm: "))
# b=int(input("nhập vào năm bạn muốn tìm:  "))
# if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
#     print("tháng có 31 ngày: ")
# elif a==4 or a==6 or a==9 or a==11:
#     print("tháng có 30 ngày: ")
# else: 
#     if  (b%400==0) or (b%4==0 and b%100!=0):
#         print("tháng có 29 ngày: ")
#     else:
#         print("tháng có 28 ngày: ")
# BÀI 21:Ngày vào ngày, tháng. Hãy tính và in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày 
# (giả sư năm đó không phải là năm nhuận)
# a=int(input("nhập vào ngày mà bạn muốn tìm: "))
# b=int(input("nhập vào tháng bạn muốn tìm:  "))
# if b<=8:
#     sothang30ngay=(b-1)//2
#     sothang31ngay=b//2
# else:
#     sothang30ngay=b//2-1
#     sothang31ngay=(b+1)//2
# songay=a+sothang30ngay*30 +sothang31ngay*31
# if b>2:
#     songay-=2
# print (songay)
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
# a=int(input("nhập điểm toán: "))
# b=int(input("nhập điểm văn: "))
# c=int(input("nhập điểm anh: "))
# if (0<=a<=10,0<=b<=10,0<=c<=10):
#      dtb= (a+b+c)/3
#      if dtb>=8 and (a>=8 or b>=8 ) and (a>=6.5,b>=6.5,c>=6.5):
#           print("học sinh giỏi:")
#      elif dtb >=6.5 and (a>=6.5 or b>=6.5 ) and (a>=5,b>=5,c>=5):
#         print("học sinh khá: ")
#      elif dtb >=5 and (a>=5 or b>=5 ) and (a>=3.5,b>=3.5,c>=3.5):
#         print("học sinh trung bình: ")
#      elif dtb >=3.5 and (a>=3.5 or b>=3.5 ) and (a>=2,b>=2,c>=2):
#          print ("học sinh yếu: ")
#      else: 
#          print("học sinh kém: ")
# else: 
#     print("bạn đã nhập sai: ")
# BÀI TẬP VÒNG LẶP FOR
# BÀI  23: In 10 lần chữ hello ra màn hình
# for i in range (1,10+1):
#     print("In 10 lần chữ hello ra màn hình")
# BÀI  24: In các số lẻ dương bé hơn 100
# for i in range(1,100,2):
#     print(i)
# BÀI  25:In các số chẵn chia hết cho 3 bé hơn 100
# for i in range(1,100,):
#     if i%3==0 and i%2==0:
#         print(i)
# BÀI  26:Nhập vào số nguyên dương a, in ra bảng cửu chương của a
# a=int(input("nhập vào số nguyên dương a để in ra bảng cửu chương a: "))
# for i in range(1,10+1):
#     print( a, "x" ,i, "=", a*i)
# BÀI  27:Viết chương trình in ra hình tam giác có độ cao h được nhập từ bàn phím
# a=int(input("nhập vào độ cao h: "))
# khoangtrangngoai= a-1
# khoangtrangtrong=1
# for i in range (a):
#     if i==0:
#         print(" " * khoangtrangngoai + "*")
#     elif i<a -1:
#         print(" " * khoangtrangngoai + "*" + " " * khoangtrangtrong + "*")
#         khoangtrangtrong += 2
#     else:
#         print("*" * (a*2-1))
#     khoangtrangngoai -= 1
# BÀI  28: Nhập vào n
# Tính S = 1 + 2 + 3 + 4 + … + n
# n=int(input("nhập vào số nguyên n: "))
# s=0
# for i in range (1,n+1):
#     s+=i
# print(s)
# BÀI  29:Nhập vào số nguyên dương a, in toàn bộ ước của a
# a=int(input("nhập vào a: "))
# for i in range(1,a+1):
#     if a%i==0:
#         print(i)
# BÀI  30: Nhập vào số nguyên dương a, đếm số ước của a
# a=int(input("nhập vào a: "))
# dem=0
# for i in range(1,a+1):
#     if a%i==0:
#         dem += 1
# print(dem)
# BÀI  31:Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
# a=int(input("nhập vào a: "))
# b=int(input("nhập vào b: "))
# for i in range (1,a+1):
#     if i>b:
#         break
#     if a%i==0 and b%i==0:
#         print(i)
# BÀI  32:Nhập vào số nguyên dương a và b, in ước chung lớn nhất của a và b
# a=int(input("nhập vào a: "))
# b=int(input("nhập vào b: "))
# ucln=1
# for i in range (1,a+1):
#     if i>b:
#         break
#     if a%i==0 and b%i==0:
#         ucln=i
# print(ucln)
# BÀI  33:Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không
# a=int(input("nhập số nguyên a: "))
# if a>1 :
#     dem=0
#     for i in range (1,a+1):
#         if a%i==0:
#             dem+=1
#     if dem==2:
#         print("đây là số nguyên tố: ")
#     else:
#         print("không phải số nguyên tố: ")
# else:
#      print("không phải số nguyên tố: ")
# BÀI TẬP VÒNG LẶP WHILE
# BÀI  34: Nhập vào số nguyên dương a, nếu nhập số âm thì yêu cầu nhập lại cho đến khi người dùng nhập đúng số dương
# Nếu người dùng nhập đúng số dương thì in ra “Bạn nhập đúng quy tắc”
# a=int(input("nhập số nguyên a: "))
# while a<=0:
#     a=int(input("bạn nhập lại số nguyên: "))
# print("bạn đã nhập đúng: ")
# BÀI  35: Nhập n
# Cho S(k) = 1 + 2 + 3 + … + k
# Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n
# a=int(input("nhập số nguyên a: "))
# s=0
# k=1
# while s<a:
#     s+=k
#     k+=1
# print(k-2)
# BÀI  36:Nhập vào A, tìm n nhỏ nhất sao cho
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A
# a=float(input("nhập vào a: "))  # đây là số thực 
# s=0
# k=1
# while s<=a:
#     s+=1/k
#     k+=1
# print(k-1)
# BÀI  37:Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1.
# Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập
# a=int(input("nhập số nguyên a: "))
# max= None
# min= None
# while a != -1:
#     if max == None or max<a:
#         max= a
#     if min == None or min >a:
#         min = a
#     a=int(input("nhập số nguyên a: "))
# print("số lớn nhất là: ",max)
# print("số nhỏ nhất là: ",min)
# BÀI  38:Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số
# a=int(input("nhập số nguyên a: "))
# a=str(a)
# dem= len(a)
# print("số này có",dem,"chữ số.")
# BÀI  39:Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ
# s=int(input("nhập vào n: "))
# demchan=demle=0
# while s != 0:
#     a=s%10
#     s=s//10
#     if a%2==0:
#         demchan+=1
#     else:
#         demle+=1
# print("tổng chữ số chẵn là: ",demchan)
# print("tổng chữ số lẻ là: ",demle)
# BÀI 40:Nhập vào số nguyên dương n, tính tổng các chữ số của n
# s=int(input("nhập vào số bất kỳ: "))
# a=0
# while s!=0:
#     n=s%10
#     s=s//10 
#     a += n
# print("tổng các chữ số bằng: ",a)
# BÀI  41: Nhập vào một số nguyên dương n, kiểm tra xem n có phải là số dạng 2^k hay không
# n=int(input("nhập số nguyên n: "))
# n0=n
# while n%2==0:
#     n=n/2
# if n==1:
#     print(n0,"là số dạng 2^k: ")
# else:
#     print(n0,"không phải số dạng 2^k: ")
# BÀI  43: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu từ (quy định là chuỗi không có ký tự đặc biệt,
# không số, không có dấu câu, chỉ có ký tự chữ và khoảng trắng)
# a=input("nhập vào một chuỗi : ")
# chuoi= a.count(" ")
# print(chuoi+1)
# BÀI TẬP XỬ LÝ CHUỖI
# BÀI  44: Nhập vào một chuỗi, hãy in từ đầu tiên trong chuỗi
# chuoi = input("nhập vào một chuỗi: ")
# a = chuoi.find(" ")
# tudautien = chuoi[:a]
# print(tudautien)
# BÀI 44 B: không in ra từ cuối cùng của chuỗi 
# chuoi = input("Nhập vào một chuỗi: ")
# a = chuoi. rfind(" ")
# chuoi0 = chuoi[ :a]
# print(chuoi0)
# chuoi = input("Nhập vào một chuỗi: ")
# chuoi_list = chuoi.split(" ")  # Tách chuỗi thành các từ
# chuoi0 = " ".join(chuoi_list[:-1])  # Nối lại các từ trừ từ cuối cùng
# print(chuoi0)
# BÀI 45: Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên cách nhau một dấu phẩy, hãy tính tổng 3 số nguyên đó
# chuoi = input("nhập vào một chuỗi có ba số nguyên: ")
# a = chuoi.find(",")
# b = chuoi.rfind(",")
# so1 = int(chuoi[:a])
# so2 = int(chuoi[a+1:b])
# so3 = int(chuoi[b+1])
# print(so1 + so2 + so3)
# BÀI 46: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số
# chuoi = input("nhập vào một chuỗi: ")
# demhoa = demthuong = demso = 0
# for i in chuoi :
#     if i.isupper():
#         demhoa += 1
#     elif i.islower():
#         demthuong += 1
#     elif i.isnumeric ():
#         demso += 1 
# print("số ký tự in hoa là: ",demhoa)   
# print("số ký tự in thường là: ",demthuong)   
# print("số ký tự số là: ",demso)   
# BÀI 47:Nhập vào một chuỗi, hãy tách toàn bộ ký tự số trong chuỗi ra rồi tính tổng của chúng
# VD:
# Nhập chuỗi: abd45ecf47wde3s1
# Tổng: 4 + 5 + 4 + 7 + 3 + 1 = 24
# chuoi = input("nhập vào chuỗi: ")
# tong = 0
# for i in chuoi:
#     if i.isnumeric():
#         tong += int(i)
# print(tong) 
# BÀI 49:Nhập vào một chuỗi, hãy tách toàn bộ con số trong chuỗi ra rồi tính tổng của chúng
# VD:
# Nhập chuỗi: abd45ecf47wde3s1
# Tổng: 45 + 47 + 3 + 1 = 96
# chuoi = input("nhập vào một chuỗi: ")
# chuoitam = ""
# tong = 0
# for i in chuoi :
#     if i.isnumeric():
#         chuoitam += i 
#     else:
#         if chuoitam != "":
#             tong += int(chuoitam)
#             chuoitam = ""
# if chuoitam != "":
#     tong += int(chuoitam)
# print(tong)
# BÀI 50: Nhập vào một chuỗi, kiểm tra chuỗi đó có phải là một chuỗi mật khẩu mạnh hay không 
# (một chuỗi mật khẩu mạnh cần có ít nhất 1 ký tự đặc biệt, 1 ký tự in hoa, 1 con số, 1 chữ thường và độ dài phải lớn hơn 6)
# chuoi = input ("nhập vào một chuỗi kiểm tra thử mật khẩu có mạnh hay không: ")
# ktdodai = len(chuoi) > 6
# ktdacbiet = ktinthuong = ktinhoa = ktso = False
# for i in chuoi :
#     if i.isnumeric():
#         ktso = True
#     elif i.isupper():
#         ktinhoa = True
#     elif i.islower():
#         ktinthuong = True
#     else:
#         ktdacbiet = True
# if ktdodai and ktso and ktinthuong and ktinhoa:
#     print("đây là mật khẩu mạnh: ")
# else:
#     print("đây là mật khẩu yếu: ")
# BÀI 51: Nhập vào một số nguyên, hãy chuyển số sang chuỗi, rồi đặt dấu chấm phân tách mỗi 3 chữ số (phân cách phần ngàn) rồi in ra màn hình
# VD: Nhập số: 375469485
# Đổi sang chuỗi rồi in ra: 375.469.485
# a = int(input("nhập vào số nguyên: "))
# a = str(a)
# i = len(a) - 3      
# while i > 0:
#     a = a[:i] + "." + a[i:]
#     i -= 3
# print(a)
# BÀI 52:Nhập vào chuỗi a và chuỗi b Hãy xóa chuỗi b trong chuỗi a rồi in lại chuỗi a ra màn hình (không dùng hàm replace)
# Ví dụ: Chuỗi a: "Xin chào mọi người!"
# Chuỗi b: "Xin chào"
# Sau khi xóa, chuỗi a: " mọi người!"
# a = input("nhập vào chuỗi a: ")
# b = input("nhập vào chuỗi b: ")
# vt_dau = 0
# vt_cuoi = len(b)    
# while vt_cuoi <= len(a):
#     if a[vt_dau:vt_cuoi] == b:
#        a = a[:vt_dau] + a[vt_cuoi:]
#     else:
#         vt_dau += 1
#         vt_cuoi += 1
# print(a)
# BÀI TẬP XỬ LÝ LIST
