#bai 1:
class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hien_thi(self):
        print(f"Toa do: ({self.x}, {self.y})")
class DiemMau(Diem):
    def __init__(self, x, y, mau):
        super().__init__(x, y)  # gọi constructor lớp cha
        self.mau = mau

# Override (ghi đè)
    def hien_thi(self):
        print(f"Toa do: ({self.x}, {self.y}) - Mau: {self.mau}")     
#khởi tạo đối tượng   
if __name__ == "__main__":
    A = Diem(1, 3)
    B = DiemMau(5, 3, "xanh")

    print("Diem A:")
    A.hien_thi()

    print("Diem B:")
    B.hien_thi()

    #bai 2:
class SinhVien:
    def __init__(self, mssv, hoten):
        self.mssv = mssv
        self.hoten = hoten
        self.mon_hoc = {}  # {ten_mon: diem}

    def dang_ky_mon(self, ten_mon, diem):
        self.mon_hoc[ten_mon] = diem

    def tinh_diem_trung_binh(self):
        if not self.mon_hoc:
            return 0
        return sum(self.mon_hoc.values()) / len(self.mon_hoc)

    def __str__(self):
        return f"{self.mssv} - {self.hoten} - ĐTB: {self.tinh_diem_trung_binh():.2f}"

class SinhVienCNTT(SinhVien):
    def __init__(self, mssv, hoten, tai_khoan, mat_khau, email):
        super().__init__(mssv, hoten)  # gọi lớp cha
        self.tai_khoan = tai_khoan
        self.mat_khau = mat_khau
        self.email = email

    # Override __str__
    def __str__(self):
        return (f"{self.mssv} - {self.hoten} - ĐTB: {self.tinh_diem_trung_binh():.2f} | "
                f"TK: {self.tai_khoan} | Email: {self.email}")
#test
if __name__ == "__main__":
    sv = SinhVienCNTT("001", "Nguyen Van A", "an123", "123456", "an@gmail.com")

    sv.dang_ky_mon("Toan", 8)
    sv.dang_ky_mon("Ly", 9)

    print(sv)

#bai 3:
class Convat:
    def __init__(self, ten):
        self.ten = ten

    def keu(self):
        print("con vật kêu: ")

class Bo(Convat):
    def keu(self):
        print("Moo")
class Heo(Convat):
    def keu(self):
        print("Oink")
class De(Convat):
    def keu(self):
        print("Bee")
class Ga(Convat):
    def keu(self):
        print("ò ó o")

if __name__ == "__main__":
    ds = [
        Bo("Bò 1"),
        Heo("Heo 1"),
        De("Dê 1"),
        Ga("Gà 1")
    ]

    print("Âm thanh nông trại: ")

    for con in ds:
        con.keu()   