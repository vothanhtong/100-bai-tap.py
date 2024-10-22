# # Bài 89: Một người dùng số tiền là U đô-la và V Euro để mua một loại nguyên liệu sản xuất.

# # Có N công ty nước ngoài bán nguyên liệu trên được đánh số từ 1 đến N. Công ty thứ i có giá bán Ai đô la/1 kg nguyên liệu và Bi Euro/1 kg nguyên liệu.

# # Tuy nhiên, tại mỗi công ty chỉ bán nguyên liệu cho một khách hàng hoặc theo đô-la, hoặc theo Euro.

# # Hãy giúp người đó tìm cách chọn ra 2 công ty để mua hàng sao cho số lượng nguyên liệu sản xuất có thể mua được là nhiều nhất.

# # Nhập vào: U, V và List A và List B

# # In ra: Số lượng nguyên liệu S (kg) người đó mua được với 2 chữ số thập phân.
# def so_luong_nguyen_lieu(U, V, A, B):
#     N = len(A)  # Số lượng công ty
    
#     max_nguyen_lieu = 0.0  # Lượng nguyên liệu lớn nhất

#     # Duyệt qua tất cả các cặp công ty i và j (i != j)
#     for i in range(N):
#         for j in range(N):
#             if i != j:  # Chỉ xét khi i và j là hai công ty khác nhau
#                 # Tính lượng nguyên liệu có thể mua từ công ty i (bằng đô-la) và công ty j (bằng Euro)
#                 so_luong = (U / A[i]) + (V / B[j])
                
#                 # Cập nhật số lượng nguyên liệu lớn nhất nếu tìm thấy giá trị lớn hơn
#                 if so_luong > max_nguyen_lieu:
#                     max_nguyen_lieu = so_luong
#     return round(max_nguyen_lieu, 2)  # Trả về số lượng với 2 chữ số thập phân
# # Ví dụ sử dụng:
# U = 1000  # Số tiền đô-la
# V = 800   # Số tiền Euro
# A = [50, 60, 70]  # Giá bán đô-la/kg của các công ty
# B = [40, 30, 50]  # Giá bán Euro/kg của các công ty
# ket_qua = so_luong_nguyen_lieu(U, V, A, B)
# print(ket_qua)  # Kết quả sẽ là số lượng nguyên liệu lớn nhất với 2 chữ số thập phân
