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