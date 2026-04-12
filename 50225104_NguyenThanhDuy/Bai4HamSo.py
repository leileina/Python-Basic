from abc import ABC, abstractmethod
import math

# 1. Class trừu tượng - Đóng vai trò là "khung" cho mọi hàm số
class HamSo(ABC):
    @abstractmethod
    def gia_tri(self, x):
        pass

    @abstractmethod
    def dao_ham(self, x):
        pass

# 2. Class con: Hàm bậc nhất y = ax + b
class HamBacNhat(HamSo):
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    # Ghi đè phương thức tính giá trị
    def gia_tri(self, x):
        return self.a * x + self.b

    # Đạo hàm của ax + b luôn bằng a
    def dao_ham(self, x):
        return self.a

    # Tìm nghiệm: ax + b = 0 => x = -b/a
    def tim_nghiem(self):
        if self.a == 0:
            return "Vô nghiệm" if self.b != 0 else "Vô số nghiệm"
        return -self.b / self.a

# 3. Class con: Hàm bậc hai y = ax^2 + bx + c
class HamBacHai(HamSo):
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def gia_tri(self, x):
        return self.a * (x**2) + self.b * x + self.c

    def dao_ham(self, x):
        return 2 * self.a * x + self.b

    # Tìm nghiệm bằng Delta
    def tim_nghiem(self):
        if self.a == 0:
            return "Đây là hàm bậc nhất, không phải bậc hai!"
        
        delta = self.b**2 - 4 * self.a * self.c
        print(f"--- Tính Delta = {delta} ---")
        
        if delta < 0:
            return "Phương trình vô nghiệm thực"
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return f"Phương trình có nghiệm kép x = {x}"
        else:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return f"Phương trình có 2 nghiệm: x1 = {x1}, x2 = {x2}"

# 4. Vẽ đồ thị (Sử dụng matplotlib - Thư viện sinh viên hay dùng nhất)
def ve_do_thi(ham_so, label="Hàm số"):
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Tạo 100 điểm từ -10 đến 10 để vẽ đường cong
    x = np.linspace(-10, 10, 100)
    y = [ham_so.gia_tri(val) for val in x]
    
    plt.plot(x, y, label=label)
    plt.axhline(0, color='black', lw=1) # Trục Ox
    plt.axvline(0, color='black', lw=1) # Trục Oy
    plt.legend()
    plt.grid(True)
    plt.title("Đồ thị hàm số")
    plt.show()

# --- CHƯƠNG TRÌNH CHÍNH ---
print("--- KIỂM TRA HÀM BẬC HAI ---")
f2 = HamBacHai(1, -3, 2) # y = x^2 - 3x + 2
print(f"Giá trị tại x = 5 là: {f2.gia_tri(5)}")
print(f"Đạo hàm tại x = 5 là: {f2.dao_ham(5)}")
print(f"Kết quả tìm nghiệm: {f2.tim_nghiem()}")

# Nếu muốn vẽ đồ thị thì bỏ comment dòng dưới (cần cài pip install matplotlib)
# ve_do_thi(f2, "y = x^2 - 3x + 2")