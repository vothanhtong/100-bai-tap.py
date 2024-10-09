# BÀI TẬP VÒNG LẶP WHILE
# BÀI  34: Nhập vào số nguyên dương a, nếu nhập số âm thì yêu cầu nhập lại cho đến khi người dùng nhập đúng số dương
# Nếu người dùng nhập đúng số dương thì in ra “Bạn nhập đúng quy tắc”
a=int(input("nhập số nguyên a: "))
while a<=0:
    a=int(input("bạn nhập lại số nguyên: "))
print("bạn đã nhập đúng: ")