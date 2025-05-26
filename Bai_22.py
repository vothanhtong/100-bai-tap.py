# BÀI 22: Nhập điểm Toán, Văn, Anh và xét loại học sinh

def xep_loai_hoc_sinh(toan, van, anh):
    # Kiểm tra điểm hợp lệ
    if not (0 <= toan <= 10 and 0 <= van <= 10 and 0 <= anh <= 10):
        return "Bạn đã nhập sai điểm. Mỗi điểm phải nằm trong khoảng từ 0 đến 10."

    # Tính điểm trung bình
    dtb = (toan + van + anh) / 3
    diem_thap_nhat = min(toan, van, anh)

    # Xét loại học sinh
    if dtb >= 8 and (toan >= 8 or van >= 8) and diem_thap_nhat >= 6.5:
        return "Học sinh giỏi"
    elif dtb >= 6.5 and (toan >= 6.5 or van >= 6.5) and diem_thap_nhat >= 5:
        return "Học sinh khá"
    elif dtb >= 5 and (toan >= 5 or van >= 5) and diem_thap_nhat >= 3.5:
        return "Học sinh trung bình"
    elif dtb >= 3.5 and (toan >= 3.5 or van >= 3.5) and diem_thap_nhat >= 2:
        return "Học sinh yếu"
    else:
        return "Học sinh kém"

# Nhập điểm từ người dùng
try:
    toan = float(input("Nhập điểm Toán (0-10): "))
    van = float(input("Nhập điểm Văn (0-10): "))
    anh = float(input("Nhập điểm Anh (0-10): "))
    
    # In kết quả
    ket_qua = xep_loai_hoc_sinh(toan, van, anh)
    print(ket_qua)
except ValueError:
    print("Vui lòng nhập số hợp lệ (dạng số thực).")
