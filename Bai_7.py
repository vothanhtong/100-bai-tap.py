# BÀI 7: Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
print(a%2==0 or b%2==0 )
# # cách 2:
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
if a%2==0 or b%2==0: 
    print("TRUE")
else:
    print("FALSE")

def kiem_tra_chia_het_cho_2(a, b):
    """
    Kiểm tra nếu 1 trong 2 số a hoặc b chia hết cho 2.
    Args:
        a (int): Số nguyên thứ nhất.
        b (int): Số nguyên thứ hai.
    Returns:
        bool: True nếu 1 trong 2 số chia hết cho 2, ngược lại False.
    """
    return a % 2 == 0 or b % 2 == 0

def main():
    try:
        # Nhập số nguyên từ người dùng
        a = int(input("Nhập vào số nguyên a: "))
        b = int(input("Nhập vào số nguyên b: "))
        
        # Kiểm tra và in kết quả
        if kiem_tra_chia_het_cho_2(a, b):
            print("TRUE - Ít nhất một trong hai số chia hết cho 2.")
        else:
            print("FALSE - Không có số nào chia hết cho 2.")
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()