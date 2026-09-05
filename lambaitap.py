
#nhập thông tin chuyến đi
ten_khach_hang = input("Minh Anh: ")
quang_duong = float(input("100 (km): "))
gio_xuat_phat = int(input("10 (giờ): "))
loai_xe = input("7 chỗ: ")
troi_mua = input("Có mưa không? (co/khong): ")

#kiểm tra tính hợp lệ
if not ten_khach_hang:
    print("Tên khách hàng không được để trống.")
elif quang_duong <= 0:
    print("Quãng đường phải lớn hơn 0.")
elif gio_xuat_phat < 0 or gio_xuat_phat > 23:
    print("Giờ xuất phát không hợp lệ.")
elif loai_xe not in ["4 chỗ", "7 chỗ"]:
    print("Loại xe không hợp lệ.")
elif troi_mua not in ["co", "khong"]:
    print("Thông tin thời tiết không hợp lệ.")

#tính toán chi phí
if loai_xe == "4 chỗ":
    chi_phi = quang_duong * 12000
elif loai_xe == "7 chỗ":
    chi_phi = quang_duong * 15000

print(f"Chi phí chuyến đi của {ten_khach_hang} là: {chi_phi} VND")
#Phụ thu giờ cao điểm; 6-8h hoặc 17-19h, phụ thu thêm 10% chi phí
if (6 <= gio_xuat_phat <= 8) or (17 <= gio_xuat_phat <= 19):
    phu_thu_gio_cao_diem = chi_phi * 0.1
    print(f"Phụ thu giờ cao điểm: {phu_thu_gio_cao_diem} VND")
else:
    phu_thu_gio_cao_diem = 0
#Nếu trời mưa, phụ thu thêm 5.000đ cho mỗi km
if troi_mua == "co":
    phu_thu_troi_mua = quang_duong * 5000
    print(f"Phụ thu trời mưa: {phu_thu_troi_mua} VND")
else:
    phu_thu_troi_mua = 0

tong_chi_phi = chi_phi + (phu_thu_gio_cao_diem if 'phu_thu_gio_cao_diem' in locals() else 0) + phu_thu_troi_mua
print(f"Tổng chi phí chuyến đi: {tong_chi_phi} VND")

#4 Phân loại chuyến đi  
if quang_duong < 5:
    print("Chuyến ngắn")
elif 5 <= quang_duong <= 15:
    print("Chuyến trung bình")
else:
    print("Chuyến dài")
#đánh giá mức độ ưu tiên của chuyến đi
gio_cao_diem = (6 <= gio_xuat_phat <= 8) or (17 <= gio_xuat_phat <= 19)
loai_chuyen_di = "chuyến dài" if quang_duong > 15 else "chuyến trung bình" if quang_duong >= 5 else "chuyến ngắn"
if gio_cao_diem:
    print("Chuyến đi diễn ra vào giờ cao điểm")
if loai_chuyen_di == "chuyến dài":
    print("Chuyến đi dài, ưu tiên tài xế có kinh nghiệm")
elif loai_chuyen_di == "chuyến trung bình":
    print("Chuyến đi trung bình, ưu tiên tài xế gần nhất")
else:
    print("Chuyến đi ngắn, tài xế bình thường")

#đánh giá mức cước
if tong_chi_phi > 150000:
    print("Mức cước cao")
else:
    print("Mức cước thấp")
