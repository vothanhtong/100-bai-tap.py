# Bài 98:Một doanh nhân, sau khi thực hiện mua bán N (N ≤ 100) chuyến hàng, mỗi chuyến hàng có tổng giá trị mua M và tổng giá trị bán B (M, B có thể lên đến 20 chữ số) mới tính xem mình huề vốn, lời hay lỗ, bao nhiêu tiền. Hãy viết chương trình để giúp doanh nhân trên tính toán kết quả kinh doanh.
# File kinhdoanh.inp:
# - Dòng đầu tiên trong file chứa số N
# - N dòng tiếp theo, mỗi dòng chứa cặp số M và B, hai số này cách nhau một khoảng trắng
# Ghi ra file kinhdoanh.out số tiền lời (nếu lỗ in ra số âm)
# VD:
# kinhdoanh.inp	kinhdoanh.out
# 5
# 50 65
# 150 141
# 15 30
# 121 200
# 300 300	100
# def tinh_ket_qua_kinh_doanh(input_file, output_file):
#     with open(input_file, 'r') as inp:
#         N = int(inp.readline().strip())  # Đọc số chuyến hàng N
#         tong_mua = 0  # Khởi tạo tổng giá trị mua
#         tong_ban = 0  # Khởi tạo tổng giá trị bán
        
#         # Đọc từng cặp M và B và tính tổng
#         for _ in range(N):
#             M, B = map(int, inp.readline().strip().split())
#             tong_mua += M
#             tong_ban += B

#     # Tính lợi nhuận
#     loi_nhuan = tong_ban - tong_mua

#     # Ghi kết quả vào file
#     with open(output_file, 'w') as out:
#         out.write(str(loi_nhuan) + '\n')

# # Sử dụng hàm với file cụ thể
# tinh_ket_qua_kinh_doanh('kinhdoanh.inp', 'kinhdoanh.out')