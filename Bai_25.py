# BÀI  25:In các số chẵn chia hết cho 3 bé hơn 100
for i in range(1,100,):
    if i%3==0 and i%2==0:
        print(i)


# BÀI 25: In các số chẵn chia hết cho 3 bé hơn 100
def in_so_chan_chia_het_cho_3():
    """
    In ra các số chẵn chia hết cho 3 và nhỏ hơn 100.
    """
    print("Các số chẵn chia hết cho 3 bé hơn 100 là:")
    for i in range(2, 100, 2):  # Duyệt qua các số chẵn
        if i % 3 == 0:
            print(i, end=" ")
    print("\n")  # Xuống dòng sau khi in xong

# BÀI 25.1: In các số lẻ chia hết cho 5 bé hơn 100
def in_so_le_chia_het_cho_5():
    """
    In ra các số lẻ chia hết cho 5 và nhỏ hơn 100.
    """
    print("Các số lẻ chia hết cho 5 bé hơn 100 là:")
    for i in range(1, 100, 2):  # Duyệt qua các số lẻ
        if i % 5 == 0:
            print(i, end=" ")
    print("\n")  # Xuống dòng sau khi in xong

# BÀI 25.2: In các số vừa chia hết cho 2 vừa chia hết cho 7 bé hơn 100
def in_so_chia_het_cho_2_va_7():
    """
    In ra các số vừa chia hết cho 2 vừa chia hết cho 7 và nhỏ hơn 100.
    """
    print("Các số vừa chia hết cho 2 vừa chia hết cho 7 bé hơn 100 là:")
    for i in range(2, 100, 2):  # Duyệt qua các số chẵn
        if i % 7 == 0:
            print(i, end=" ")
    print("\n")  # Xuống dòng sau khi in xong

# BÀI 25.3: In các số nguyên tố bé hơn 100
def in_so_nguyen_to():
    """
    In ra các số nguyên tố nhỏ hơn 100.
    """
    print("Các số nguyên tố bé hơn 100 là:")
    for num in range(2, 100):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    print("\n")  # Xuống dòng sau khi in xong

# Gọi các hàm để chạy chương trình
if __name__ == "__main__":
    in_so_chan_chia_het_cho_3()
    in_so_le_chia_het_cho_5()
    in_so_chia_het_cho_2_va_7()
    in_so_nguyen_to()