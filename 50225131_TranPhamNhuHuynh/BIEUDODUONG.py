# Import thư viện matplotlib để vẽ biểu đồ
import matplotlib.pyplot as plt

# ===== CLASS BIỂU ĐỒ ĐƯỜNG =====
class BieuDoDuong:

    # Hàm khởi tạo (constructor)
    def __init__(self, thang, doanh_thu):
        self.thang = thang            # Danh sách các tháng (trục X)
        self.doanh_thu = doanh_thu    # Danh sách doanh thu (trục Y)

    # ===== HIỂN THỊ DỮ LIỆU =====
    def hien_thi_du_lieu(self):
        print("Danh sách tháng:", self.thang)        # In danh sách tháng
        print("Danh sách doanh thu:", self.doanh_thu) # In danh sách doanh thu

    # ===== VẼ BIỂU ĐỒ =====
    def ve_bieu_do(self):

        # Vẽ biểu đồ đường (line chart)
        plt.plot(self.thang, self.doanh_thu, marker='o')
        # marker='o' giúp hiển thị các điểm dữ liệu bằng chấm tròn

        # Thêm tiêu đề cho biểu đồ
        plt.title("Biểu đồ doanh thu 6 tháng đầu năm")

        # Đặt tên cho trục X
        plt.xlabel("Tháng")

        # Đặt tên cho trục Y
        plt.ylabel("Doanh thu (triệu đồng)")

        # Hiển thị lưới giúp dễ nhìn giá trị hơn
        plt.grid(True)

        # Hiển thị biểu đồ ra màn hình
        plt.show()


# ===== CHƯƠNG TRÌNH CHÍNH =====

# Tạo dữ liệu mẫu
thang = ["T1", "T2", "T3", "T4", "T5", "T6"]   # 6 tháng đầu năm
doanh_thu = [12, 15, 14, 18, 20, 22]          # Doanh thu tương ứng

# Tạo đối tượng từ class
bd = BieuDoDuong(thang, doanh_thu)

# Hiển thị dữ liệu
bd.hien_thi_du_lieu()

# Vẽ biểu đồ
bd.ve_bieu_do()