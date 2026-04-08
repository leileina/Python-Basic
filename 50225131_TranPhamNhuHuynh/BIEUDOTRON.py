import matplotlib.pyplot as plt

# ===== CLASS BIỂU ĐỒ TRÒN =====
class BieuDoTron:
    def __init__(self, khoan_chi, so_tien):
        self.khoan_chi = khoan_chi      # các khoản chi
        self.so_tien = so_tien          # số tiền tương ứng

    # ===== HIỂN THỊ DỮ LIỆU =====
    def hien_thi_du_lieu(self):
        print("Khoản chi:", self.khoan_chi)
        print("Số tiền:", self.so_tien)

    # ===== VẼ BIỂU ĐỒ TRÒN =====
    def ve_bieu_do(self):
        plt.pie(
            self.so_tien,
            labels=self.khoan_chi,
            autopct='%1.1f%%'   # hiển thị phần trăm
        )

        plt.title("Cơ cấu chi tiêu hằng tháng")
        plt.show()


# ===== CHƯƠNG TRÌNH CHÍNH =====
khoan_chi = ["Ăn uống", "Đi lại", "Học tập", "Giải trí"]
so_tien = [2000000, 500000, 1000000, 700000]

bd = BieuDoTron(khoan_chi, so_tien)

bd.hien_thi_du_lieu()
bd.ve_bieu_do()