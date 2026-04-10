from abc import ABC, abstractmethod

# 1. Class trừu tượng - "Khung" cho mọi biểu thức
class BieuThuc(ABC):
    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def to_string(self):
        pass

# 2. Class Số - Đây là các "Nút lá" (không có con bên dưới)
class So(BieuThuc):
    def __init__(self, gia_tri):
        self.gia_tri = float(gia_tri)

    def evaluate(self):
        return self.gia_tri

    def to_string(self):
        # Trả về số dưới dạng chuỗi (để ghép vào biểu thức)
        if self.gia_tri.is_integer():
            return str(int(self.gia_tri))
        return str(self.gia_tri)

# 3. Class trung gian cho các phép toán 2 ngôi (+, -, *, /)
# Sinh viên thường dùng class này để tránh lặp lại code gán left/right
class BinaryOp(BieuThuc):
    def __init__(self, left, right):
        self.left = left   # Có thể là một So hoặc một BieuThuc khác (đệ quy)
        self.right = right

# 4. Các class phép toán cụ thể
class Cong(BinaryOp):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()
    
    def to_string(self):
        return f"({self.left.to_string()} + {self.right.to_string()})"

class Tru(BinaryOp):
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()
    
    def to_string(self):
        return f"({self.left.to_string()} - {self.right.to_string()})"

class Nhan(BinaryOp):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()
    
    def to_string(self):
        return f"({self.left.to_string()} * {self.right.to_string()})"

class Chia(BinaryOp):
    def evaluate(self):
        mau = self.right.evaluate()
        if mau == 0:
            raise Exception("Lỗi: Không thể chia cho 0 trong biểu thức!")
        return self.left.evaluate() / mau
    
    def to_string(self):
        return f"({self.left.to_string()} / {self.right.to_string()})"

# --- (TEST) ---

if __name__ == "__main__":
    # Tạo cây biểu thức theo đúng yêu cầu: 3 + (4 * 5)
    # Cấu trúc:
    #       Cong
    #      /    \
    #    So(3)  Nhan
    #          /    \
    #        So(4)  So(5)

    node3 = So(3)
    node4 = So(4)
    node5 = So(5)

    nhan_4_5 = Nhan(node4, node5)       # (4 * 5)
    bieu_thuc_chinh = Cong(node3, nhan_4_5) # 3 + (4 * 5)

    print("--- KẾT QUẢ ---")
    print(f"Biểu thức chuỗi: {bieu_thuc_chinh.to_string()}")
    print(f"Giá trị cuối cùng: {bieu_thuc_chinh.evaluate()}")

    # Test thêm biểu thức phức tạp hơn: (10 - 2) * (5 + 1)
    bt_phuc_tap = Nhan(Tru(So(10), So(2)), Cong(So(5), So(1)))
    print(f"Phức tạp: {bt_phuc_tap.to_string()} = {bt_phuc_tap.evaluate()}")