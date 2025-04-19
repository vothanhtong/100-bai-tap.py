# BÀI 6: Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
# CÁCH 1: 
a=int(input("nhập vào số nguyên a: "))
if a%5==0 and not 20<=a<=70:
    print("TRUE")
else:

    print("FALSE")
# # CÁCH 2:
a=int(input("nhập vào số nguyên a: "))
print(a%5==0 and not 20<=a<=70)
def kiem_tra_so(a):
    """
    Kiểm tra xem số a có chia hết cho 5 nhưng không nằm trong khoảng từ 20 đến 70 hay không.
    Args:
        a (int): Số nguyên cần kiểm tra.
    Returns:
        bool: True nếu thỏa mãn điều kiện, ngược lại False.
    """
    return a % 5 == 0 and not 20 <= a <= 70


def main():
    try:
        # Nhập số nguyên từ người dùng
        a = int(input("Nhập vào số nguyên a: "))
        
        # Kiểm tra và in kết quả
        if kiem_tra_so(a):
            print("TRUE - Số chia hết cho 5 và không nằm trong khoảng từ 20 đến 70.")
        else:
            print("FALSE - Số không thỏa mãn điều kiện.")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()