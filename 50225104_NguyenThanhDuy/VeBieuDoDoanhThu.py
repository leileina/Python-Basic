import matplotlib.pyplot as plt

class BieuDoDuong:
    """Lớp để quản lý và vẽ biểu đồ đường doanh thu 6 tháng"""

    def __init__(self, thang=None, doanh_thu=None):
        """Hàm khởi tạo

        Parameters:
        - thang: danh sách tháng
        - doanh_thu: danh sách doanh thu
        """
        self.thang = thang if thang is not None else []
        self.doanh_thu = doanh_thu if doanh_thu is not None else []

    def hien_thi_du_lieu(self):
        """Hiển thị dữ liệu tháng và doanh thu."""
        if not self.thang or not self.doanh_thu:
            print("Không có dữ liệu để hiển thị!")
            return

        print("\n" + "=" * 50)
        print("DANH SÁCH DOANH THU 6 THÁNG")
        print("=" * 50)
        for thang, doanh_thu in zip(self.thang, self.doanh_thu):
            print(f"{thang:3} - Doanh thu: {doanh_thu}")
        print("=" * 50 + "\n")

    def ve_bieu_do(self):
        """Vẽ biểu đồ đường doanh thu."""
        if not self.thang or not self.doanh_thu:
            print("Không có dữ liệu để vẽ biểu đồ!")
            return

        plt.figure(figsize=(10, 6))
        plt.plot(self.thang, self.doanh_thu, marker='o', linestyle='-', color='tab:blue')
        plt.title('Biểu Đồ Đường Doanh Thu 6 Tháng Đầu Năm', fontsize=16, fontweight='bold')
        plt.xlabel('Tháng', fontsize=12)
        plt.ylabel('Doanh thu (triệu đồng)', fontsize=12)
        plt.grid(alpha=0.3, linestyle='--')

        for i, value in enumerate(self.doanh_thu):
            plt.text(i, value + 0.3, str(value), ha='center', va='bottom')

        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    thang = ["T1", "T2", "T3", "T4", "T5", "T6"]
    doanh_thu = [12, 15, 14, 18, 20, 22]

    bieu_do = BieuDoDuong(thang, doanh_thu)
    bieu_do.hien_thi_du_lieu()
    bieu_do.ve_bieu_do()
