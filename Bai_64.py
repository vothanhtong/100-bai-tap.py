def is_odd_pair_list(seq):
    """
    Kiểm tra xem một list số nguyên có phải là 'list chẵn lẻ' (sum của mọi cặp  = lẻ) không.
    Điều kiện: Với mọi cặp (i, j), seq[i] + seq[j] là số lẻ.
    Suy ra: list tối đa 2 phần tử và phải có đúng 1 chẵn + 1 lẻ (hoặc <2 phần tử).
    """
    n = len(seq)
    if n < 2:
        return True  # 0 hoặc 1 phần tử: không có cặp để kiểm tra, hợp lệ
    # Đếm số chẵn và lẻ
    evens = sum(1 for x in seq if x % 2 == 0)
    odds  = n - evens
    # Muốn mọi cặp là chẵn+lẻ => không được có 2 chẵn hay 2 lẻ
    return (evens == 1 and odds == 1)

def main():
    try:
        data = input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ")
        L = list(map(int, data.split()))
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập các số nguyên hợp lệ.")
        return

    print(f"Danh sách đã nhập: {L}")

    if is_odd_pair_list(L):
        print("→ Đây là list chẵn lẻ (mọi cặp cộng lại đều lẻ).")
    else:
        print("→ Không phải list chẵn lẻ.")
        # Giải thích ngắn:
        evens = [x for x in L if x % 2 == 0]
        odds  = [x for x in L if x % 2 != 0]
        if len(L) >= 2:
            if len(evens) > 1:
                print(f"  • Có {len(evens)} số chẵn: {evens}, nên tồn tại cặp chẵn+chẵn ⇒ tổng chẵn.")
            if len(odds) > 1:
                print(f"  • Có {len(odds)} số lẻ: {odds}, nên tồn tại cặp lẻ+lẻ ⇒ tổng chẵn.")

if __name__ == "__main__":
    main()
