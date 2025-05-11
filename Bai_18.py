# BÀI 18: Giải và biện luận phương trình ax + b = 0
a = int(input("nhập vào số nguyên a: "))
b = int(input("nhập vào số nguyên b: "))
print ("phương trình" + str(a) + "x+" + str(b)+"=0" )
if a == 0:
    if b == 0:
        print("phương trình vô số nghiệm: ")
    else:
        print("phương trình vô nghiệm: ")
else:
    print("nghiệm của phương trình là: ",-b/a)  

def nhap_so_nguyen(thong_bao):
    while True:
        try:
            return int(input(thong_bao))
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")

def giai_phuong_trinh_bac_nhat():
    a = nhap_so_nguyen("Nhập vào số nguyên a: ")
    b = nhap_so_nguyen("Nhập vào số nguyên b: ")
    print(f"Phương trình: {a}x + {b} = 0")
    if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -b / a
        print(f"Nghiệm của phương trình là: x = {x:.2f}")

if __name__ == "__main__":
    while True:
        giai_phuong_trinh_bac_nhat()
        tiep_tuc = input("Bạn có muốn giải phương trình khác không? (y/n): ").lower()
        if tiep_tuc != 'y':
            print("Kết thúc chương trình.")
            break