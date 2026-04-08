
class PhanSo:
    def __init__(self, tu_so, mau_so):
        if mau_so == 0:
            raise ValueError("Mẫu số không được bằng 0")
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.rut_gon()

# Rút gọn phân số
    def rut_gon(self):
        
        self.tu_so
        self.mau_so 
# Đảm bảo mẫu luôn dương
        if self.mau_so < 0:
            self.tu_so *= -1
            self.mau_so *= -1

# Nghịch đảo
    def nghich_dao(self):
        return PhanSo(self.mau_so, self.tu_so)

# Giá trị thực
    def gia_tri_thuc(self):
        return self.tu_so / self.mau_so

# Phép cộng
    def __add__(self, other):
        tu = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau)

# Phép trừ
    def __sub__(self, other):
        tu = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau)

# Phép nhân
    def __mul__(self, other):
        return PhanSo(self.tu_so * other.tu_so,
                      self.mau_so * other.mau_so)

# Phép chia
    def __truediv__(self, other):
        return self * other.nghich_dao()

# So sánh <
    def __lt__(self, other):
        return self.gia_tri_thuc() < other.gia_tri_thuc()

# In đẹp
    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"
    
class SDPhanSo:
    def __init__(self):
        self.ds = []

    def nhap(self):
        n = int(input("Nhập số lượng phân số: "))
        for i in range(n):
            print(f"\nPhân số {i+1}:")
            tu = int(input("Tử số: "))
            mau = int(input("Mẫu số: "))
            ps = PhanSo(tu, mau)
            self.ds.append(ps)

    def tim_max(self):
        return max(self.ds)

    def tinh_tong(self):
        tong = PhanSo(0, 1)
        for ps in self.ds:
            tong = tong + ps
        return tong

    def hien_thi(self):
        print("\nDanh sách phân số:")
        for ps in self.ds:
            print(ps)

        print("\nPhân số lớn nhất:", self.tim_max())
        print("Tổng các phân số:", self.tinh_tong())

if __name__ == "__main__":
    app = SDPhanSo()
    app.nhap()
    app.hien_thi()