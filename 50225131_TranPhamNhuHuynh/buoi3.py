#bài 1:
class Gach:
    def __init__(self, ma, mau, so_luong_hop, chieu_dai, chieu_ngang, gia):
        self.ma = ma
        self.mau = mau
        self.so_luong_hop = so_luong_hop
        self.chieu_dai = chieu_dai  # cm
        self.chieu_ngang = chieu_ngang  # cm
        self.gia = gia  # giá 1 hộp

    # Giá mỗi viên
    def gia_ban_le(self):
        return self.gia / self.so_luong_hop

    # Diện tích tối đa 1 hộp (m2)
    def dien_tich_nen_toi_da(self):
        dien_tich_1_vien = (self.chieu_dai * self.chieu_ngang) / 10000
        return dien_tich_1_vien * self.so_luong_hop

    # Số hộp cần cho nền D x N (m)
    def so_luong_hop(self, D, N):
        tong_dt = D * N
        return int(tong_dt / self.dien_tich_nen_toi_da() + 1)

    # Giá trên mỗi m2
    def gia_m2(self):
        return self.gia / self.dien_tich_nen_toi_da()
ds = [
    Gach("G1", "Do", 10, 30, 30, 200000),
    Gach("G2", "Xanh", 8, 40, 40, 250000),
]
#key là 1 hàm dùng để xác đinh tiêu chí so sánh
#lấy phần tử ,áp dụng hàm key ,so sánh kết quả trả về
re_nhat = min(ds, key=lambda g: g.gia_m2())#Nhận vào 1 phần tử g (một viên gạch trong danh sách ds)
                                            #Trả về: g.gia_m2() (giá trên mỗi m² của viên gạch đó)
print("Gạch rẻ nhất:", re_nhat.ma)

#bai 2:
import math
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class DoanThang:
    def __init__(self, d1, d2):
        self.d1 = d1  # object Diem
        self.d2 = d2

    def tinh_do_dai(self):
        return math.sqrt((self.d1.x - self.d2.x)**2 +
                         (self.d1.y - self.d2.y)**2)

    def tinh_goc_voi_truc_hoanh(self):
        dx = self.d2.x - self.d1.x
        dy = self.d2.y - self.d1.y
        return math.degrees(math.atan2(dy, dx)) #atan2 trả về radian,dg là hàm trg thư viện py
#test
A = Diem(0, 0)
B = Diem(3, 4)

dt = DoanThang(A, B)

print("Độ dài:", dt.tinh_do_dai())
print("Góc:", dt.tinh_goc_voi_truc_hoanh())   

#bài 3:
class Date:
    def __init__(self, ngay, thang, nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

class SinhVien:
    def __init__(self, mssv, hoten, ngaysinh):
        self.mssv = mssv
        self.hoten = hoten
        self.ngaysinh = ngaysinh  # object Date
        self.mon_hoc = {}  # {ten_mon: diem}

    def dang_ky_mon(self, ten_mon, diem):
        self.mon_hoc[ten_mon] = diem

    def xoa_mon(self, ten_mon):
        if ten_mon in self.mon_hoc:
            del self.mon_hoc[ten_mon]

    def tinh_diem_trung_binh(self):
        if not self.mon_hoc:
            return 0
        return sum(self.mon_hoc.values()) / len(self.mon_hoc)

    def __str__(self):#đoạn chuỗi
        return "{self.mssv} - {self.hoten} - ĐTB: {self.tinh_diem_trung_binh()}"
    
ds = []


sv1 = SinhVien("001", "Ngoc", Date(1,1,2000))
sv1.dang_ky_mon("Toan", 8)
sv1.dang_ky_mon("Ly", 7)

sv2 = SinhVien("002", "Binh", Date(2,2,2000))
sv2.dang_ky_mon("Toan", 9)
sv2.dang_ky_mon("Ly", 9)

ds.append(sv1)
ds.append(sv2)

# Tìm ĐTB cao nhất
max_sv = max(ds, key=lambda sv: sv.tinh_diem_trung_binh())
print("Sinh viên giỏi nhất:", max_sv)

# Sắp xếp theo tên
ds.sort(key=lambda sv: sv.hoten)

print("\nDanh sách sau sắp xếp:")
for sv in ds:
    print(sv)    

