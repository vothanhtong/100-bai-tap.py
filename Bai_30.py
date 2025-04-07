# BÀI  30: Nhập vào số nguyên dương a, đếm số ước của a
a=int(input("nhập vào a: "))
dem=0
for i in range(1,a+1):
    if a%i==0:
        dem += 1
print(dem)

# BÀI 31: Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không
a = int(input("Nhập vào số nguyên dương a: "))
if a < 2:
    print("Không phải là số nguyên tố")
else:
    is_prime = True
    for i in range(2, int(a**0.5) + 1):  # Kiểm tra từ 2 đến căn bậc hai của a
        if a % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Đây là số nguyên tố")
    else:
        print("Không phải là số nguyên tố")