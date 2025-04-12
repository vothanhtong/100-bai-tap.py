from collections import Counter

# Bài 87: Tìm các phần tử xuất hiện nhiều hơn k lần trong danh sách
def tim_phan_tu_xuat_hien_hon_k(L, k):
    """
    Hàm tìm các phần tử xuất hiện nhiều hơn k lần trong danh sách L.

    Args:
        L (list): Danh sách các số nguyên dương.
        k (int): Số lần xuất hiện tối thiểu.

    Returns:
        list: Danh sách các phần tử xuất hiện nhiều hơn k lần, sắp xếp tăng dần.
    """
    # Kiểm tra đầu vào
    if not all(isinstance(x, int) and x > 0 for x in L):
        raise ValueError("Danh sách L phải chứa toàn số nguyên dương.")
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k phải là một số nguyên dương.")

    # Đếm số lần xuất hiện của từng phần tử
    dem = Counter(L)

    # Lọc các phần tử xuất hiện nhiều hơn k lần
    L_kq = [num for num, count in dem.items() if count > k]

    # Sắp xếp danh sách kết quả theo thứ tự tăng dần
    return sorted(L_kq)

# Ví dụ sử dụng
L = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
k = 2
L_kq = tim_phan_tu_xuat_hien_hon_k(L, k)
print(L_kq)  # Kết quả sẽ là [3, 4]