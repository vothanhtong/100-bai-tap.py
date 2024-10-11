# BÀI 62: Nhập vào một list số nguyên L, hãy kiểm tra xem L có phải là một cấp số cộng hay không? Nếu có thì tìm và in ra công sai, nếu không có thì in ra None
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Hàm kiểm tra cấp số cộng và tìm công sai
def is_arithmetic_sequence(seq):
    if len(seq) < 2:
        return None  # Không đủ phần tử để xác định

    common_difference = seq[1] - seq[0]  # Tính công sai ban đầu
    for i in range(2, len(seq)):
        if seq[i] - seq[i - 1] != common_difference:
            return None  # Không phải cấp số cộng

    return common_difference  # Trả về công sai nếu là cấp số cộng

# Kiểm tra và in ra kết quả
common_difference = is_arithmetic_sequence(L)
if common_difference is not None:
    print("List là một cấp số cộng với công sai:", common_difference)
else:
    print(None)