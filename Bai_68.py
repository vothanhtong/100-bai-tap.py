# BÀI 68 : Nhập vào một list số nguyên L, hãy biến đổi L bằng cách thay đổi vị trí giữa giá trị nhỏ nhất và lớn nhất
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Kiểm tra list không rỗng
if not L:
    print("List rỗng!")
else:
    # Tìm chỉ số của giá trị nhỏ nhất và lớn nhất
    min_index = L.index(min(L))
    max_index = L.index(max(L))

    # Hoán đổi giá trị nhỏ nhất và lớn nhất
    L[min_index], L[max_index] = L[max_index], L[min_index]

    # In ra list đã biến đổi
    print("List sau khi hoán đổi:", L)

    def hoan_doi_min_max(L):
    # """
    # Hoán đổi vị trí giữa giá trị nhỏ nhất và lớn nhất trong danh sách.
    # Args:
    #     L (list): Danh sách các số nguyên.
    # Returns:
    #     list: Danh sách sau khi hoán đổi.
    # """
    # if len(L) <= 1:
        print("Danh sách chỉ có một phần tử hoặc rỗng, không cần hoán đổi.")
        return L

    # Tìm chỉ số của giá trị nhỏ nhất và lớn nhất
    min_index = L.index(min(L))
    max_index = L.index(max(L))

    # Hoán đổi giá trị nhỏ nhất và lớn nhất
    L[min_index], L[max_index] = L[max_index], L[min_index]
    # return L

def main():
    try:
        # Nhập danh sách số nguyên từ người dùng
        L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

        if not L:
            print("Danh sách rỗng!")
        else:
            print(f"Giá trị nhỏ nhất: {min(L)}, Giá trị lớn nhất: {max(L)}")
            # Hoán đổi và in kết quả
            L = hoan_doi_min_max(L)
            print("Danh sách sau khi hoán đổi:", L)
    except ValueError:
        print("Lỗi: Vui lòng nhập danh sách các số nguyên hợp lệ.")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()