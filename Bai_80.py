def is_prime(n):
    """Kiểm tra số nguyên tố."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_first_a_primes(L, a):
    """
    Trả về danh sách gồm 'a' số nguyên tố đầu tiên xuất hiện trong list L.
    Nếu không đủ thì trả về tất cả số nguyên tố tìm được.
    """
    if not isinstance(L, list) or not isinstance(a, int) or a <= 0:
        raise ValueError("Danh sách L phải là list và a phải là số nguyên dương.")

    # Lọc và giữ nguyên thứ tự xuất hiện
    primes = [num for num in L if isinstance(num, int) and is_prime(num)]

    # Trả về tối đa a phần tử
    return primes[:a]

# Ví dụ sử dụng
L = [10, 3, 5, 8, 2, 7, 15, 19, 11]
a = 5
print(get_first_a_primes(L, a))  # Output: [3, 5, 2, 7, 19]



# Bài tập 1: Đếm số nguyên tố trong danh sách
# Viết hàm count_primes(L) trả về số lượng các số nguyên tố trong danh sách L.

# Ví dụ: count_primes([2, 4, 5, 6, 7, 8]) → 3
def count_primes(L):
    """Đếm số lượng số nguyên tố trong danh sách L."""
    if not isinstance(L, list):
        raise ValueError("Danh sách L phải là list.")

    # Đếm số nguyên tố
    return sum(1 for num in L if isinstance(num, int) and is_prime(num))
# c2:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(L):
    return sum(1 for num in L if is_prime(num))

# Ví dụ sử dụng
L = [2, 4, 5, 6, 7, 8]
print(count_primes(L))  # Output: 3


