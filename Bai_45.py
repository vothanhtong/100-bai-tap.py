# BÀI 45: Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên cách nhau một dấu phẩy, hãy tính tổng 3 số nguyên đó
chuoi = input("nhập vào một chuỗi có ba số nguyên: ")
a = chuoi.find(",")
b = chuoi.rfind(",")
so1 = int(chuoi[:a])
so2 = int(chuoi[a+1:b])
so3 = int(chuoi[b+1])
print(so1 + so2 + so3)