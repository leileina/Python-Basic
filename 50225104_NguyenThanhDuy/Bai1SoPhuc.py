import math

class SoPhuc:
    def __init__(self, real, imag):
        # Ép kiểu float ngay từ đầu cho chắc chắn
        self.real = float(real)
        self.imag = float(imag)

    # In ra màn hình: 3.0 + 4.0i
    def __str__(self):
        dau = "+" if self.imag >= 0 else "-"
        return f"{self.real} {dau} {abs(self.imag)}i"

    # Tính độ lớn (trị tuyệt đối) số phức
    def module(self):
        return math.sqrt(self.real**2 + self.imag**2)

    # Số phức liên hợp: đảo dấu phần ảo
    def conjugate(self):
        return SoPhuc(self.real, -self.imag)

    # --- NẠP CHỒNG TOÁN TỬ ---

    # Phép cộng: (a + c) + (b + d)i
    def __add__(self, other):
        return SoPhuc(self.real + other.real, self.imag + other.imag)

    # Phép trừ: (a - c) + (b - d)i
    def __sub__(self, other):
        return SoPhuc(self.real - other.real, self.imag - other.imag)

    # Phép nhân: (ac - bd) + (ad + bc)i
    def __mul__(self, other):
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return SoPhuc(r, i)

    # Phép chia: Nhân tử và mẫu cho số liên hợp của mẫu
    def __truediv__(self, other):
        mau = other.real**2 + other.imag**2
        if mau == 0:
            raise Exception("Lỗi: Mẫu số bằng 0 không thể chia!")
        
        tu_thuc = (self.real * other.real + self.imag * other.imag) / mau
        tu_ao = (self.imag * other.real - self.real * other.imag) / mau
        return SoPhuc(tu_thuc, tu_ao)

# ---(TEST) ---
if __name__ == "__main__":
    sp1 = SoPhuc(3, 4)
    sp2 = SoPhuc(1, 2)

    print(f"Số phức 1 là: {sp1}")
    print(f"Số phức 2 là: {sp2}")
    print(f"Tổng: {sp1 + sp2}")
    print(f"Hiệu: {sp1 - sp2}")
    print(f"Tích: {sp1 * sp2}")
    print(f"Thương: {sp1 / sp2}")
    print(f"Module của sp1: {sp1.module()}")
    print(f"Số liên hợp của sp1: {sp1.conjugate()}")