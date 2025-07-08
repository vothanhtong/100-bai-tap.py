# Bài 94: Cho một chuỗi ký tự S (gồm chữ và số). Hãy viết chương trình tách chữ và số thành hai chuỗi riêng biệt.
# File chuoi.inp chứa duy nhất 1 chuỗi S

# Hãy tách và ghi vào file chuoi.out 2 dòng, dòng thứ nhất ghi chuỗi ký tự chữ, dòng thứ hai ghi chuỗi ký tự số.

# Nếu như chuỗi nào rỗng thì ghi dấu trừ ‘-’.
# VD1:
# chuoi.inp	chuoi.out
# a1B2c34d	aBcd
# 1234
# VD2:
# chuoi.inp	chuoi.out
# abghcGGG	abghcGGG
# def tach_chu_so(input_file, output_file):
#     with open(input_file, 'r') as inp, open(output_file, 'w') as out:
#         chuoi = inp.read().strip()  # Đọc chuỗi S từ file và loại bỏ ký tự trắng thừa
        
#         chuoi_chu = ""
#         chuoi_so = ""

#         # Duyệt qua từng ký tự trong chuỗi
#         for ky_tu in chuoi:
#             if ky_tu.isalpha():  # Nếu là chữ cái
#                 chuoi_chu += ky_tu
#             elif ky_tu.isdigit():  # Nếu là chữ số
#                 chuoi_so += ky_tu

#         # Nếu chuỗi nào rỗng, thay bằng dấu '-'
#         if not chuoi_chu:
#             chuoi_chu = "-"
#         if not chuoi_so:
#             chuoi_so = "-"
        
#         # Ghi kết quả vào file, mỗi chuỗi trên một dòng
#         out.write(chuoi_chu + "\n")
#         out.write(chuoi_so + "\n")

# # Sử dụng hàm với file cụ thể
# tach_chu_so('chuoi.inp', 'chuoi.out')
def tach_chu_so(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as inp:
        chuoi = inp.read().strip()

    chuoi_chu = ''.join([c for c in chuoi if c.isalpha()]) or '-'
    chuoi_so = ''.join([c for c in chuoi if c.isdigit()]) or '-'

    with open(output_file, 'w', encoding