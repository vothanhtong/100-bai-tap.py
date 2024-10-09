# BÀI TẬP XỬ LÝ CHUỖI
# BÀI  44 A: Nhập vào một chuỗi, hãy in từ đầu tiên trong chuỗi
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