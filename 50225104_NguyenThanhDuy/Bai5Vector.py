import math

class Vector:
    def __init__(self, toa_do):
        # toa_do là một danh sách các số: [1, 2, 3]
        self.data = [float(x) for x in toa_do]

    def __str__(self):
        return f"Vector({self.data})"

    # 1. Phép cộng hai vector: [a1+b1, a2+b2, ...]
    def __add__(self, other):
        if len(self.data) != len(other.data):
            raise Exception("Lỗi: Hai vector phải cùng kích thước!")
        
        kq = []
        for i in range(len(self.data)):
            kq.append(self.data[i] + other.data[i])
        return Vector(kq)

    # 2. Phép trừ hai vector: [a1-b1, a2-b2, ...]
    def __sub__(self, other):
        if len(self.data) != len(other.data):
            raise Exception("Lỗi: Hai vector phải cùng kích thước!")
        
        kq = [self.data[i] - other.data[i] for i in range(len(self.data))]
        return Vector(kq)

    # 3. Tích vô hướng (Dot product): a1*b1 + a2*b2 + ...
    def dot(self, other):
        if len(self.data) != len(other.data):
            raise Exception("Lỗi: Không thể tính tích vô hướng khác kích thước!")
        
        tong = 0
        for i in range(len(self.data)):
            tong += self.data[i] * other.data[i]
        return tong

    # 4. Độ dài (Norm): căn bậc hai của tổng bình phương các phần tử
    def norm(self):
        tong_bp = sum([x**2 for x in self.data])
        return math.sqrt(tong_bp)

    # --- YÊU CẦU NÂNG CAO ---

    # Tính góc giữa 2 vector (đơn vị: độ)
    def goc_giua(self, other):
        # Công thức: cos(alpha) = (A.B) / (|A| * |B|)
        tu = self.dot(other)
        mau = self.norm() * other.norm()
        
        if mau == 0:
            return 0
            
        cos_alpha = tu / mau
        # Tránh lỗi sai số máy tính khiến cos > 1 hoặc < -1
        cos_alpha = max(-1, min(1, cos_alpha))
        
        radian = math.acos(cos_alpha)
        return math.degrees(radian)

    # Kiểm tra vuông góc
    def la_vuong_goc(self, other):
        # Nếu tích vô hướng bằng 0 thì vuông góc
        return self.dot(other) == 0

# --- TEST ---
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([1, 0])
v4 = Vector([0, 1])

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"Tổng v1 + v2: {v1 + v2}")
print(f"Tích vô hướng v1.v2: {v1.dot(v2)}")
print(f"Độ dài v1: {v1.norm():.2f}")

print("-" * 30)
print(f"Góc giữa v3 và v4: {v3.goc_giua(v4)} độ")
print(f"v3 có vuông góc v4 không? {v3.la_vuong_goc(v4)}")