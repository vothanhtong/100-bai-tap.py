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