# Dãy số fibonacci là dãy số được định nghĩa như sau: 1, 1, 2, 3, 5, 8, 13,... với số kế tiếp sẽ bằng tổng hai số trước đó
# Nhập vào A, hãy tìm số trong dãy số fibonacci lớn nhất nhưng không vượt quá A
# Hàm tìm số Fibonacci lớn nhất không vượt quá A
def fibonacci_max(A):
    # Khởi tạo các số đầu tiên trong dãy Fibonacci
    fib1, fib2 = 1, 1

    # Tìm số Fibonacci lớn nhất nhỏ hơn hoặc bằng A
    while fib2 <= A:
        fib1, fib2 = fib2, fib1 + fib2

    # Trả về số Fibonacci lớn nhất nhỏ hơn hoặc bằng A
    return fib1

# Nhập vào giá trị A
A = int(input("Nhập A: "))

# Tìm và in ra kết quả
print("Số Fibonacci lớn nhất không vượt quá A là:", fibonacci_max(A))
