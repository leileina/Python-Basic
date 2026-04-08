# Import thư viện matplotlib để vẽ biểu đồ
import matplotlib.pyplot as plt

# Tạo class (lớp) biểu đồ cột
class BieuDoCot:

    # Hàm khởi tạo (constructor)
    def __init__(self, ten, diem):
        self.ten = ten      # Danh sách tên sinh viên
        self.diem = diem    # Danh sách điểm tương ứng

    # ===== NHẬP DỮ LIỆU =====
    def nhap_du_lieu(self):
        n = int(input("Nhập số lượng sinh viên: "))  # Nhập số lượng SV

        # Duyệt từng sinh viên
        for i in range(n):
            ten = input(f"Nhập tên sinh viên {i+1}: ")   # Nhập tên
            diem = float(input(f"Nhập điểm của {ten}: "))  # Nhập điểm

            self.ten.append(ten)   # Thêm tên vào danh sách
            self.diem.append(diem) # Thêm điểm vào danh sách

    # ===== HIỂN THỊ DỮ LIỆU =====
    def hien_thi(self):
        print("\nDanh sách sinh viên:")

        # Duyệt theo chỉ số
        for i in range(len(self.ten)):
            print(self.ten[i], "-", self.diem[i])  # In tên và điểm

    # ===== VẼ BIỂU ĐỒ =====
    def ve_bieu_do(self):
        plt.bar(self.ten, self.diem)  # Vẽ biểu đồ cột

        plt.title("Biểu đồ điểm sinh viên")  # Tiêu đề
        plt.xlabel("Tên sinh viên")          # Trục X
        plt.ylabel("Điểm")                  # Trục Y

        plt.show()  # Hiển thị biểu đồ


# ===== CHƯƠNG TRÌNH CHÍNH =====

# Dữ liệu mẫu ban đầu
ten = ["An", "Binh", "Lan", "Minh", "Ha"]
diem = [8, 7, 9, 6, 10]

# Tạo đối tượng từ class
bd = BieuDoCot(ten, diem)

# Cách 1: Nhập dữ liệu từ bàn phím
# bd.nhap_du_lieu()

# Cách 2: Gán lại dữ liệu theo đề bài
bd.ten = ["An", "Bình", "Lan", "Minh", "Hà"]
bd.diem = [8, 7, 9, 6, 10]

# Hiển thị dữ liệu
bd.hien_thi()

# Vẽ biểu đồ
bd.ve_bieu_do()