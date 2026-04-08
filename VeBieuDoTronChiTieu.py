import matplotlib.pyplot as plt


class BieuDoTron:
    """Lớp để quản lý và vẽ biểu đồ tròn chi tiêu hàng tháng"""

    def __init__(self, khoan_chi=None, so_tien=None):
        """Hàm khởi tạo

        Parameters:
        - khoan_chi: danh sách các khoản chi
        - so_tien: danh sách số tiền tương ứng
        """
        self.khoan_chi = khoan_chi if khoan_chi is not None else []
        self.so_tien = so_tien if so_tien is not None else []

    def hien_thi_du_lieu(self):
        """Hiển thị dữ liệu chi tiêu."""
        if not self.khoan_chi or not self.so_tien:
            print("Không có dữ liệu để hiển thị!")
            return

        print("\n" + "=" * 50)
        print("DANH SÁCH CƠ CẤU CHI TIÊU")
        print("=" * 50)
        for khoan, tien in zip(self.khoan_chi, self.so_tien):
            print(f"{khoan:12} - Số tiền: {tien:,} VND")
        print("=" * 50 + "\n")

    def ve_bieu_do(self):
        """Vẽ biểu đồ tròn cơ cấu chi tiêu."""
        if not self.khoan_chi or not self.so_tien:
            print("Không có dữ liệu để vẽ biểu đồ!")
            return

        plt.figure(figsize=(8, 8))
        wedges, texts, autotexts = plt.pie(
            self.so_tien,
            labels=self.khoan_chi,
            autopct='%1.1f%%',
            startangle=140,
            colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'],
            pctdistance=0.8,
            textprops={'fontsize': 11}
        )

        for text in texts + autotexts:
            text.set_color('black')

        plt.title('Biểu Đồ Tròn Cơ Cấu Chi Tiêu', fontsize=16, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    khoan_chi = ["Ăn uống", "Đi lại", "Học tập", "Giải trí"]
    so_tien = [2000000, 500000, 1000000, 700000]

    bieu_do = BieuDoTron(khoan_chi, so_tien)
    bieu_do.hien_thi_du_lieu()
    bieu_do.ve_bieu_do()
