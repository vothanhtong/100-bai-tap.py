# Nhập vào một chuỗi, hãy tách toàn bộ ký tự số trong chuỗi ra rồi tính tổng của chúng
# VD:Nhập chuỗi: abd45ecf47wde3s1
# Tổng: 4 + 5 + 4 + 7 + 3 + 1 = 24
# Hàm tính tổng các ký tự số trong chuỗi
def sum_of_digits(s):
    total = 0
    for char in s:
        if char.isdigit():  # Kiểm tra nếu ký tự là chữ số
            total += int(char)  # Cộng giá trị số vào tổng
    return total

# Nhập vào chuỗi
s = input("Nhập chuỗi: ")

# Tính và in ra tổng
result = sum_of_digits(s)
print("Tổng các ký tự số trong chuỗi là:", result)
