def get_first_a_primes(L, a):
    primes = []  # Danh sách chứa số nguyên tố tìm được
    
    # Duyệt qua từng phần tử trong L
    for number in L:
        if is_prime(number):
            primes.append(number)  # Thêm số nguyên tố vào danh sách
            if len(primes) == a:  # Kiểm tra xem đã đủ a phần tử chưa
                break
    
    return primes  # Trả về danh sách các số nguyên tố