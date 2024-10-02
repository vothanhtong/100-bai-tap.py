# bài 1: Nhập vào số n, hãy nhân n lên cho 3, rồi cộng 1 sau đó in kết quả ra màn hình
# a=int(input("nhập vào số nguyên a: "))
# n=(a*3)+1
# print("khi a nhân cho ba và cộng cho một là: ",n)
# bài 2: Nhập vào số n, hãy mũ 2 rồi chia cho 3, sau đó in kết quả ra màn hình
# a=int(input("nhập vào số nguyên a: "))
# n=(a**2)/3
# print("số in ra màng hình là: ",n)
# bài 3:Nhập vào nhiệt độ c, in ra nhiệt độ F
# a=float(input("nhập vào nhiệt độ c: "))
# n=(a*1.8)+32
# print("nhiệt độ f là: ",n)
# bài 4:Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False
# a=int(input("nhập vào số nguyên a: "))
# if a%2==0:
#     print("TRUE")
# else:
#     print("FALSE")
# bài 5:  Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
# cách 1:
# a=int(input("nhập số nguyên a: "))
# if a %3 == 0 and 50<= a <=100:
#     print("TRUE")
# else:
#     print("FALSE")
# cách 2:
# a=int(input("nhập vào số nguyên a: "))
# print(a%3==0 and 50<=a<=100)
# bài 6: Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
# CÁCH 1: 
# a=int(input("nhập vào số nguyên a: "))
# if a%5==0 and not 20<=a<=70:
#     print("TRUE")
# else:

#     print("FALSE")
# # CÁCH 2:
# a=int(input("nhập vào số nguyên a: "))
# print(a%5==0 and not 20<=a<=70)
# bài 7: Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
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
# bài 8: Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False
# a=float(input("nhập vào một số a: "))
# b=round(a)
# print(a==b )
# bài 9:Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False
# a=int(input("nhập số nguyên a:  "))
# cana=a**0.5
# print(cana==round(cana))
# bài 10:Nhập vào lương tháng này nhận được, ta phải đưa cho vợ 90% số tiền lương đó. Hãy in ra lương ta giữ lại
# a=int(input("nhập vào lương tháng này bạn nhận được: "))
# print("lương giữ lại còn: ",a*0.1)
# bài 10:Nhập vào 3 số a, b, c. In ra kết quả là tổng của ba số đó
# a=int(input("nhập vào số nguyên a: "))
# b=int(input("nhập vào số nguyên b: "))
# c=int(input("nhập vào số nguyên c: "))
# tong=a+b+c
# print("tổng ba số a,b,a là: ",tong)
# bài 12: Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c
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
# bài 13:Nhập vào số nguyên dương a, nếu a lớn hơn 10 thì ta in ra đây là số lớn hơn 10
# a=int(input("nhập vào số nguyên a: "))
# if a>10 :
#     print("đây là số lớn hơn 10: ")
# else:
#     print("đây là số nhỏ hơn 10: ")
# bài 14: Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ
# a=int(input("nhập vào số nguyên dương a: "))
# print("số này đặc biệt: ")
# if a%2==0:
#     print("đây là số chẵn ")
# else:
#     print("đây là số lẻ: ")
# bài 15 và 16 :))) :Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không
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
# bài 17: Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại
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
#  bài 18: Giải và biện luận phương trình ax + b = 0
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
# bài 19: Giải và biện luận phương trình ax^2 + bx + c = 0
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
# bài 20 :Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày
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
# bài 21:Ngày vào ngày, tháng. Hãy tính và in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày (giả sư năm đó không phải là năm nhuận)
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
# bài 22: Nhập điểm toán, văn, anh.
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
# bài 23: In 10 lần chữ hello ra màn hình
# for i in range (1,10+1):
#     print("In 10 lần chữ hello ra màn hình")
# bài 24: In các số lẻ dương bé hơn 100
# for i in range(1,100,2):
#     print(i)
# bài 25:In các số chẵn chia hết cho 3 bé hơn 100
# for i in range(1,100,):
#     if i%3==0 and i%2==0:
#         print(i)
# bài 26:Nhập vào số nguyên dương a, in ra bảng cửu chương của a
# a=int(input("nhập vào số nguyên dương a để in ra bảng cửu chương a: "))
# for i in range(1,10+1):
#     print( a, "x" ,i, "=", a*i)
# bài 27:Viết chương trình in ra hình tam giác có độ cao h được nhập từ bàn phím
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
# bài 28: Nhập vào n
# Tính S = 1 + 2 + 3 + 4 + … + n
# n=int(input("nhập vào số nguyên n: "))
# s=0
# for i in range (1,n+1):
#     s+=i
# print(s)
# bài 29:Nhập vào số nguyên dương a, in toàn bộ ước của a
# a=int(input("nhập vào a: "))
# for i in range(1,a+1):
#     if a%i==0:
#         print(i)
# bài 30: Nhập vào số nguyên dương a, đếm số ước của a
# a=int(input("nhập vào a: "))
# dem=0
# for i in range(1,a+1):
#     if a%i==0:
#         dem += 1
# print(dem)
#  bài 31:Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
# a=int(input("nhập vào a: "))
# b=int(input("nhập vào b: "))
# for i in range (1,a+1):
#     if i>b:
#         break
#     if a%i==0 and b%i==0:
#         print(i)
# bài 32:Nhập vào số nguyên dương a và b, in ước chung lớn nhất của a và b
# a=int(input("nhập vào a: "))
# b=int(input("nhập vào b: "))
# ucln=1
# for i in range (1,a+1):
#     if i>b:
#         break
#     if a%i==0 and b%i==0:
#         ucln=i
# print(ucln)
# bài 33:Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không
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
# bài 34: Nhập vào số nguyên dương a, nếu nhập số âm thì yêu cầu nhập lại cho đến khi người dùng nhập đúng số dương
# Nếu người dùng nhập đúng số dương thì in ra “Bạn nhập đúng quy tắc”
# a=int(input("nhập số nguyên a: "))
# while a<=0:
#     a=int(input("bạn nhập lại số nguyên: "))
# print("bạn đã nhập đúng: ")
# bài 35: Nhập n
# Cho S(k) = 1 + 2 + 3 + … + k
# Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n
# a=int(input("nhập số nguyên a: "))
# s=0
# k=1
# while s<a:
#     s+=k
#     k+=1
# print(k-2)
# bài 36:Nhập vào A, tìm n nhỏ nhất sao cho
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A
# a=float(input("nhập vào a: "))  # đây là số thực 
# s=0
# k=1
# while s<=a:
#     s+=1/k
#     k+=1
# print(k-1)
# bài 37:Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1.
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
# bài 38:Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số
# a=int(input("nhập số nguyên a: "))
# a=str(a)
# dem= len(a)
# print("số này có",dem,"chữ số.")
# bài 39:Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ
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
# bài 40:Nhập vào số nguyên dương n, tính tổng các chữ số của n
# s=int(input("nhập vào số bất kỳ: "))
# a=0
# while s!=0:
#     n=s%10
#     s=s//10 
#     a += n
# print("tổng các chữ số bằng: ",a)
# bài 41: Nhập vào một số nguyên dương n, kiểm tra xem n có phải là số dạng 2^k hay không
# n=int(input("nhập số nguyên n: "))
# n0=n
# while n%2==0:
#     n=n/2

# if n==1:
#     print(n0,"là số dạng 2^k: ")
# else:
#     print(n0,"không phải số dạng 2^k: ")
# bài 43: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu từ (quy định là chuỗi không có ký tự đặc biệt,
# không số, không có dấu câu, chỉ có ký tự chữ và khoảng trắng)
# a=input("nhập vào một chuỗi : ")
# chuoi= a.count(" ")
# print(chuoi+1)
# bài 44: Nhập vào một chuỗi, hãy in từ đầu tiên trong chuỗi

# bài 45: Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên cách nhau một dấu phẩy, hãy tính tổng 3 số nguyên đó
# VD:
# Nhập: 3, 12, 15
# Tổng: 30

# bài 46: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số