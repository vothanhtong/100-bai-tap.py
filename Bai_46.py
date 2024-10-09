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