import math

# 1. Class cha: HinhHoc
class HinhHoc:
    def dien_tich(self):
        pass

    def chu_vi(self):
        pass

# 2. Các Class con kế thừa từ HinhHoc

class HinhTron(HinhHoc):
    def __init__(self, r):
        self.r = float(r)

    def dien_tich(self):
        return math.pi * self.r**2

    def chu_vi(self):
        return 2 * math.pi * self.r

class HinhChuNhat(HinhHoc):
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def dien_tich(self):
        return self.a * self.b

    def chu_vi(self):
        return (self.a + self.b) * 2

class HinhTamGiac(HinhHoc):
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        # Kiểm tra điều kiện tam giác hợp lệ
        if not (self.a + self.b > self.c and 
                self.a + self.c > self.b and 
                self.b + self.c > self.a):
            raise Exception("Lỗi: Ba cạnh không tạo thành tam giác!")

    def chu_vi(self):
        return self.a + self.b + self.c

    def dien_tich(self):
        # Công thức Heron tính diện tích tam giác khi biết 3 cạnh
        p = self.chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

# --- ĐA HÌNH (POLYMORPHISM) ---

# Tạo danh sách các hình
ds_hinh = [
    HinhTron(3), 
    HinhChuNhat(2, 4), 
    HinhTamGiac(3, 4, 5)
]

print("--- KẾT QUẢ TÍNH TOÁN ---")
for hinh in ds_hinh:
    # Tính đa hình: Cùng gọi tên hàm dien_tich() 
    # nhưng mỗi đối tượng tự tính theo công thức riêng của nó
    ten_hinh = hinh.__class__.__name__
    print(f"{ten_hinh}: Chu vi = {hinh.chu_vi():.2f}, Diện tích = {hinh.dien_tich():.2f}")