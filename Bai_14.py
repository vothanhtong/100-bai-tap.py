# BÀI 14: Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ
a=int(input("nhập vào số nguyên dương a: "))
print("số này đặc biệt: ")
if a%2==0:
    print("đây là số chẵn ")
else:
    print("đây là số lẻ: ")

    def kiem_tra_chan_le(a):
    # """
    # Kiểm tra xem số nguyên dương a là số chẵn hay số lẻ.
    # Args:
    #     a (int): Số nguyên dương cần kiểm tra.
    # Returns:
    #     str: Chuỗi thông báo kết quả.
    # """
    # if a % 2 == 0:
    #     return "Đây là số chẵn."
    # else:
    #     return "Đây là số lẻ."

# def main():
    # try:
        # Nhập số nguyên dương từ người dùng
        a = int(input("Nhập vào số nguyên dương a: "))
        if a <= 0:
            raise ValueError("Số phải là số nguyên dương lớn hơn 0.")

        # Gọi hàm kiểm tra và in kết quả
        print(kiem_tra_chan_le(a))
    # except ValueError as e:
        # print(f"Lỗi: {e}")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()