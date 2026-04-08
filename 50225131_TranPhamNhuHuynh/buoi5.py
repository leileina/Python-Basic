class MyDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

class KhachHang:
    def __init__(self, ma_kh, ten, dia_chi):
        self.ma_kh = ma_kh
        self.ten = ten
        self.dia_chi = dia_chi

    def tinh_giam_gia(self, tong_tien):
        return 0  # khách thường không giảm

    def __str__(self):#nối chuỗi
        return f"{self.ma_kh} - {self.ten} - {self.dia_chi}"

class KhachHangVIP(KhachHang):
    def __init__(self, ma_kh, ten, dia_chi, muc_giam):
        super().__init__(ma_kh, ten, dia_chi)
        self.muc_giam = muc_giam  # %

    def tinh_giam_gia(self, tong_tien):
        return tong_tien * self.muc_giam / 100

class HoaDon:
    def __init__(self, khach_hang, ngay_lap):
        self.khach_hang = khach_hang
        self.ngay_lap = ngay_lap
        self.ds_hang = []  # mỗi phần tử: (ten, so_luong, don_gia)

    def them_hang(self, ten, so_luong, don_gia):
        self.ds_hang.append((ten, so_luong, don_gia))

    def tinh_tong_tien(self):
        tong = sum(sl * dg for _, sl, dg in self.ds_hang)
        giam = self.khach_hang.tinh_giam_gia(tong)
        return tong - giam

    def __str__(self):
        s = f"\nHÓA ĐƠN\n"
        s += f"Khách hàng: {self.khach_hang}\n"
        s += f"Ngày lập: {self.ngay_lap}\n"
        s += "Danh sách hàng:\n"
        for ten, sl, dg in self.ds_hang:
            s += f"- {ten}: {sl} x {dg} = {sl * dg}\n"
        s += f"Tổng tiền: {self.tinh_tong_tien()}\n"
        return s


# =========================
# Chương trình chính
# =========================

# tạo khách hàng
kh1 = KhachHang("KH01", "Nguyễn Thành Duy", "Cần Thơ")
kh2 = KhachHangVIP("KH02", "Phạm Thị Cẩm Linh", "HCM", 10)

# tạo hóa đơn
hd1 = HoaDon(kh1, MyDate(23, 3, 2026))
hd1.them_hang("Bút", 10, 5000)
hd1.them_hang("Vở", 5, 10000)

hd2 = HoaDon(kh2, MyDate(23, 3, 2026))
hd2.them_hang("Sách", 2, 50000)
hd2.them_hang("Cặp", 1, 150000)

# in hóa đơn
print(hd1)
print(hd2)

# danh sách khách VIP
print("\nKhách hàng VIP:")
for kh in [kh1, kh2]:
    if isinstance(kh, KhachHangVIP):
        print(kh)