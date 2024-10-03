# bài 50: Nhập vào một chuỗi, kiểm tra chuỗi đó có phải là một chuỗi mật khẩu mạnh hay không 
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