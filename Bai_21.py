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