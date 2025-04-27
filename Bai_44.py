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
# Bài 44 C: Đếm số từ trong chuỗi
def dem_so_tu(chuoi):
    """
    Đếm số từ trong chuỗi.
    """
    so_tu = len(chuoi.split())
    print(f"Số từ trong chuỗi là: {so_tu}")

chuoi = input("Nhập vào một chuỗi: ")
dem_so_tu(chuoi)
# Bài 44 D: Đảo ngược chuỗi
def dao_nguoc_chuoi(chuoi):
    """
    Đảo ngược chuỗi.
    """
    chuoi_dao_nguoc = chuoi[::-1]
    print(f"Chuỗi đảo ngược là: {chuoi_dao_nguoc}")

chuoi = input("Nhập vào một chuỗi: ")
dao_nguoc_chuoi(chuoi)
# Bài 44 E: Đảo ngược thứ tự các từ trong chuỗi
def dao_nguoc_tu(chuoi):
    """
    Đảo ngược thứ tự các từ trong chuỗi.
    """
    chuoi_dao_nguoc_tu = " ".join(chuoi.split()[::-1])
    print(f"Chuỗi với thứ tự từ đảo ngược: {chuoi_dao_nguoc_tu}")

chuoi = input("Nhập vào một chuỗi: ")
dao_nguoc_tu(chuoi)
# Bài 44 H: Đếm số lần xuất hiện của từng từ trong chuỗi
# Ví dụ chạy chương trình:

def dem_tan_suat_tu(chuoi):
    """
    Đếm số lần xuất hiện của từng từ trong chuỗi.
    """
    tu_tan_suat = {}
    for tu in chuoi.split():
        tu_tan_suat[tu] = tu_tan_suat.get(tu, 0) + 1
    print("Số lần xuất hiện của từng từ:")
    for tu, tan_suat in tu_tan_suat.items():
        print(f"{tu}: {tan_suat}")

chuoi = input("Nhập vào một chuỗi: ")
dem_tan_suat_tu(chuoi)