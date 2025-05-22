def nhap_so_nguyen(thong_bao):
    while True:
        try:
            return int(input(thong_bao))
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")

def giai_phuong_trinh_bac_hai():
    a = nhap_so_nguyen("Nhập vào số nguyên a: ")
    b = nhap_so_nguyen("Nhập vào số nguyên b: ")
    c = nhap_so_nguyen("Nhập vào số nguyên c: ")
    print(f"Phương trình: {a}x^2 + {b}x + {c} = 0")
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình vô số nghiệm.")
            else:
                print("Phương trình vô nghiệm.")
        else:
            x = -c / b
            print(f"Phương trình có một nghiệm: x = {x:.2f}")
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            sqrt_delta = delta**0.5
            x1 = (-b + sqrt_delta) / (2*a)
            x2 = (-b - sqrt_delta) / (2*a)
            print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1:.2f}, x2 = {x2:.2f}")
        elif delta == 0:
            x = -b / (2*a)
            print(f"Phương trình có nghiệm kép: x1 = x2 = {x:.2f}")
        else:
            print("Phương trình vô nghiệm.")

if __name__ == "__main__":
    while True:
        giai_phuong_trinh_bac_hai()
        tiep_tuc = input("Bạn có muốn giải phương trình khác không? (y/n): ").lower()
        if tiep_tuc != 'y':
            print("Kết thúc chương trình.")
            break