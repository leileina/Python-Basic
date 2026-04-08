import matplotlib.pyplot as plt


class BieuDo:
    """Lớp cha chứa tiêu đề biểu đồ"""

    def __init__(self, tieu_de="Biểu đồ"):
        """Hàm khởi tạo lớp cha

        Parameters:
        - tieu_de: Tiêu đề của biểu đồ
        """
        self.tieu_de = tieu_de

    def ve_bieu_do(self):
        """Phương thức trừu tượng - sẽ được ghi đè bởi các lớp con"""
        raise NotImplementedError("Lớp con phải triển khai phương thức ve_bieu_do()")


class BieuDoCot(BieuDo):
    """Lớp con vẽ biểu đồ cột điểm sinh viên"""

    def __init__(self, ten_sinh_vien=None, diem=None, tieu_de="Biểu Đồ Cột - Điểm Sinh Viên"):
        """Hàm khởi tạo lớp con

        Parameters:
        - ten_sinh_vien: Danh sách tên sinh viên
        - diem: Danh sách điểm sinh viên
        - tieu_de: Tiêu đề biểu đồ
        """
        super().__init__(tieu_de)
        self.ten_sinh_vien = ten_sinh_vien if ten_sinh_vien is not None else []
        self.diem = diem if diem is not None else []

    def nhap_du_lieu(self, ten_sinh_vien, diem):
        """Phương thức nhập dữ liệu sinh viên"""
        if len(ten_sinh_vien) != len(diem):
            print("Lỗi: Số lượng tên và điểm không khớp!")
            return False

        self.ten_sinh_vien = ten_sinh_vien
        self.diem = diem
        print("Dữ liệu đã được nhập thành công!")
        return True

    def hien_thi_du_lieu(self):
        """Phương thức hiển thị dữ liệu sinh viên"""
        if not self.ten_sinh_vien or not self.diem:
            print("Không có dữ liệu để hiển thị!")
            return

        print("\n" + "="*50)
        print("DANH SÁCH SINH VIÊN VÀ ĐIỂM")
        print("="*50)

        for ten, diem in zip(self.ten_sinh_vien, self.diem):
            print(f"{ten:15} - Điểm: {diem}")

        print("="*50 + "\n")

    def ve_bieu_do(self):
        """Ghi đè phương thức vẽ biểu đồ cột"""
        if not self.ten_sinh_vien or not self.diem:
            print("Không có dữ liệu để vẽ biểu đồ!")
            return

        # Tạo hình vẽ
        plt.figure(figsize=(10, 6))

        # Vẽ biểu đồ cột
        plt.bar(self.ten_sinh_vien, self.diem, color='steelblue', edgecolor='navy', alpha=0.7)

        # Thiết lập tiêu đề và nhãn trục
        plt.title(self.tieu_de, fontsize=16, fontweight='bold')
        plt.xlabel('Tên Sinh Viên', fontsize=12)
        plt.ylabel('Điểm', fontsize=12)

        # Thiết lập giới hạn của trục Y
        plt.ylim(0, 10)

        # Thêm lưới để dễ đọc
        plt.grid(axis='y', alpha=0.3, linestyle='--')

        # Thêm giá trị điểm trên mỗi cột
        for i, (ten, diem) in enumerate(zip(self.ten_sinh_vien, self.diem)):
            plt.text(i, diem + 0.2, str(diem), ha='center', va='bottom', fontweight='bold')

        # Điều chỉnh bố cục
        plt.tight_layout()

        # Hiển thị biểu đồ
        plt.show()


class BieuDoDuong(BieuDo):
    """Lớp con vẽ biểu đồ đường doanh thu 6 tháng"""

    def __init__(self, thang=None, doanh_thu=None, tieu_de="Biểu Đồ Đường Doanh Thu 6 Tháng Đầu Năm"):
        """Hàm khởi tạo lớp con

        Parameters:
        - thang: danh sách tháng
        - doanh_thu: danh sách doanh thu
        - tieu_de: Tiêu đề biểu đồ
        """
        super().__init__(tieu_de)
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
        """Ghi đè phương thức vẽ biểu đồ đường"""
        if not self.thang or not self.doanh_thu:
            print("Không có dữ liệu để vẽ biểu đồ!")
            return

        plt.figure(figsize=(10, 6))
        plt.plot(self.thang, self.doanh_thu, marker='o', linestyle='-', color='tab:blue')
        plt.title(self.tieu_de, fontsize=16, fontweight='bold')
        plt.xlabel('Tháng', fontsize=12)
        plt.ylabel('Doanh thu (triệu đồng)', fontsize=12)
        plt.grid(alpha=0.3, linestyle='--')

        for i, value in enumerate(self.doanh_thu):
            plt.text(i, value + 0.3, str(value), ha='center', va='bottom')

        plt.tight_layout()
        plt.show()


class BieuDoTron(BieuDo):
    """Lớp con vẽ biểu đồ tròn cơ cấu chi tiêu"""

    def __init__(self, khoan_chi=None, so_tien=None, tieu_de="Biểu Đồ Tròn Cơ Cấu Chi Tiêu"):
        """Hàm khởi tạo lớp con

        Parameters:
        - khoan_chi: danh sách các khoản chi
        - so_tien: danh sách số tiền tương ứng
        - tieu_de: Tiêu đề biểu đồ
        """
        super().__init__(tieu_de)
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
        """Ghi đè phương thức vẽ biểu đồ tròn"""
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

        plt.title(self.tieu_de, fontsize=16, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()


# ============== CHƯƠNG TRÌNH DEMO ==============
if __name__ == "__main__":
    print("=== DEMO KẾ THỪA VÀ GHI ĐÈ PHƯƠNG THỨC ===\n")

    # Demo BieuDoCot
    print("1. BIỂU ĐỒ CỘT - ĐIỂM SINH VIÊN")
    danh_sach_ten = ["An", "Bình", "Lan", "Minh", "Hà"]
    danh_sach_diem = [8, 7, 9, 6, 10]

    bieu_do_cot = BieuDoCot(danh_sach_ten, danh_sach_diem)
    bieu_do_cot.hien_thi_du_lieu()
    print("Đang vẽ biểu đồ cột...")
    bieu_do_cot.ve_bieu_do()

    # Demo BieuDoDuong
    print("\n2. BIỂU ĐỒ ĐƯỜNG - DOANH THU 6 THÁNG")
    thang = ["T1", "T2", "T3", "T4", "T5", "T6"]
    doanh_thu = [12, 15, 14, 18, 20, 22]

    bieu_do_duong = BieuDoDuong(thang, doanh_thu)
    bieu_do_duong.hien_thi_du_lieu()
    print("Đang vẽ biểu đồ đường...")
    bieu_do_duong.ve_bieu_do()

    # Demo BieuDoTron
    print("\n3. BIỂU ĐỒ TRÒN - CƠ CẤU CHI TIÊU")
    khoan_chi = ["Ăn uống", "Đi lại", "Học tập", "Giải trí"]
    so_tien = [2000000, 500000, 1000000, 700000]

    bieu_do_tron = BieuDoTron(khoan_chi, so_tien)
    bieu_do_tron.hien_thi_du_lieu()
    print("Đang vẽ biểu đồ tròn...")
    bieu_do_tron.ve_bieu_do()

    print("\n=== HOÀN THÀNH DEMO ===")
