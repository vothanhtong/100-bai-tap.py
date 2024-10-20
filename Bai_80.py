# # BÀI 80: Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a.
# #  Hãy tìm và trả về một list mới có số phần tử là a, giá trị các phần tử là các số nguyên tố tìm được trong list L
# def is_prime(n):
#     """Kiểm tra xem n có phải là số nguyên tố hay không."""
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def get_first_a_primes(L, a):
#     primes = []  # Danh sách chứa số nguyên tố tìm được
    
#     # Duyệt qua từng phần tử trong L
#     for number in L:
#         if is_prime(number):
#             primes.append(number)  # Thêm số nguyên tố vào danh sách
#             if len(primes) == a:  # Kiểm tra xem đã đủ a phần tử chưa
#                 break
    
#     return primes  # Trả về danh sách các số nguyên tố