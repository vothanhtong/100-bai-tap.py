# # BÀI 11:Nhập vào 3 số a, b, c. In ra kết quả là tổng của ba số đó
# a=int(input("nhập vào số nguyên a: "))
# b=int(input("nhập vào số nguyên b: "))
# c=int(input("nhập vào số nguyên c: "))
# tong=a+b+c
# print("tổng ba số a,b,a là: ",tong)

## BÀI: In bảng cửu chương không trùng lặp
def print_multiplication_table():
    for i in range(1, 10):  # Duyệt từ 1 đến 9
        for j in range(i, 10):  # Duyệt từ i đến 9 để tránh trùng lặp
            print(f"{i} x {j} = {i * j}")
    print("Bảng cửu chương không trùng lặp đã được in ra.")

# Gọi hàm để in bảng cửu chương
print_multiplication_table()