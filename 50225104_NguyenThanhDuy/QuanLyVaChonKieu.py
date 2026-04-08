import matplotlib.pyplot as plt


class QuanLyDuLieu:
    """Lớp quản lý dữ liệu môn học và điểm trung bình"""

    def __init__(self):
        """Hàm khởi tạo"""
        self.mon_hoc = []
        self.diem_tb = []

    def nhap_du_lieu(self, mon_hoc, diem_tb):
        """Nhập dữ liệu môn học và điểm"""
        if len(mon_hoc) != len(diem_tb):
            print("Lỗi: Số lượng môn học và điểm không khớp!")
            return False

        self.mon_hoc = mon_hoc
        self.diem_tb = diem_tb
        print("Dữ liệu đã được nhập thành công!")
        return True

    def them_mon_hoc(self, mon, diem):
        """Thêm một môn học mới"""
        self.mon_hoc.append(mon)
        self.diem_tb.append(diem)
        print(f"Đã thêm môn {mon} với điểm {diem}")

    def sua_diem(self, mon, diem_moi):
        """Sửa điểm của một môn học"""
        if mon in self.mon_hoc:
            index = self.mon_hoc.index(mon)
            self.diem_tb[index] = diem_moi
            print(f"Đã cập nhật điểm môn {mon} thành {diem_moi}")
        else:
            print(f"Không tìm thấy môn {mon}")

    def xoa_mon_hoc(self, mon):
        """Xóa một môn học"""
        if mon in self.mon_hoc:
            index = self.mon_hoc.index(mon)
            del self.mon_hoc[index]
            del self.diem_tb[index]
            print(f"Đã xóa môn {mon}")
        else:
            print(f"Không tìm thấy môn {mon}")

    def hien_thi_du_lieu(self):
        """Hiển thị dữ liệu môn học và điểm"""
        if not self.mon_hoc:
            print("Không có dữ liệu để hiển thị!")
            return

        print("\n" + "="*60)
        print("DANH SÁCH MÔN HỌC VÀ ĐIỂM TRUNG BÌNH")
        print("="*60)
        print(f"{'Môn học':<15} {'Điểm TB':<10}")
        print("-"*60)

        for mon, diem in zip(self.mon_hoc, self.diem_tb):
            print(f"{mon:<15} {diem:<10.1f}")

        print("="*60 + "\n")

    def lay_du_lieu(self):
        """Trả về dữ liệu để vẽ biểu đồ"""
        return self.mon_hoc, self.diem_tb


class VeBieuDo:
    """Lớp vẽ biểu đồ"""

    def __init__(self, quan_ly_du_lieu):
        """Hàm khởi tạo

        Parameters:
        - quan_ly_du_lieu: Đối tượng QuanLyDuLieu
        """
        self.quan_ly = quan_ly_du_lieu

    def ve_bieu_do_cot(self):
        """Vẽ biểu đồ cột"""
        mon_hoc, diem_tb = self.quan_ly.lay_du_lieu()

        if not mon_hoc:
            print("Không có dữ liệu để vẽ biểu đồ!")
            return

        plt.figure(figsize=(12, 6))
        bars = plt.bar(mon_hoc, diem_tb, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
                      alpha=0.8, edgecolor='black', linewidth=1)

        plt.title('Biểu Đồ Cột - Điểm Trung Bình Các Môn Học', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Môn Học', fontsize=12)
        plt.ylabel('Điểm Trung Bình', fontsize=12)
        plt.ylim(0, 10)

        # Thêm giá trị trên mỗi cột
        for bar, diem in zip(bars, diem_tb):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    f'{diem:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=10)

        plt.grid(axis='y', alpha=0.3, linestyle='--')
        plt.tight_layout()
        plt.show()

    def ve_bieu_do_duong(self):
        """Vẽ biểu đồ đường"""
        mon_hoc, diem_tb = self.quan_ly.lay_du_lieu()

        if not mon_hoc:
            print("Không có dữ liệu để vẽ biểu đồ!")
            return

        plt.figure(figsize=(12, 6))
        plt.plot(mon_hoc, diem_tb, marker='o', linestyle='-', linewidth=3, markersize=8,
                color='#2E86AB', markerfacecolor='#A23B72', markeredgecolor='black')

        plt.title('Biểu Đồ Đường - Điểm Trung Bình Các Môn Học', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Môn Học', fontsize=12)
        plt.ylabel('Điểm Trung Bình', fontsize=12)
        plt.ylim(0, 10)

        # Thêm giá trị tại mỗi điếm
        for i, (mon, diem) in enumerate(zip(mon_hoc, diem_tb)):
            plt.text(i, diem + 0.15, f'{diem:.1f}', ha='center', va='bottom',
                    fontweight='bold', fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

        plt.grid(alpha=0.3, linestyle='--')
        plt.tight_layout()
        plt.show()


class MenuChinh:
    """Lớp quản lý menu chính của chương trình"""

    def __init__(self):
        """Hàm khởi tạo"""
        self.quan_ly_du_lieu = QuanLyDuLieu()
        self.ve_bieu_do = VeBieuDo(self.quan_ly_du_lieu)

        # Dữ liệu mẫu
        self.khoi_tao_du_lieu_mau()

    def khoi_tao_du_lieu_mau(self):
        """Khởi tạo dữ liệu mẫu"""
        mon_hoc_mau = ["Toán", "Lý", "Hóa", "Tin", "Anh"]
        diem_tb_mau = [7.5, 8.0, 6.8, 9.1, 7.9]
        self.quan_ly_du_lieu.nhap_du_lieu(mon_hoc_mau, diem_tb_mau)

    def hien_thi_menu(self):
        """Hiển thị menu chính"""
        print("\n" + "="*70)
        print("           CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM VÀ VẼ BIỂU ĐỒ")
        print("="*70)
        print("1. Hiển thị dữ liệu môn học")
        print("2. Thêm môn học mới")
        print("3. Sửa điểm môn học")
        print("4. Xóa môn học")
        print("5. Vẽ biểu đồ cột")
        print("6. Vẽ biểu đồ đường")
        print("0. Thoát chương trình")
        print("="*70)

    def chay_chuong_trinh(self):
        """Chạy chương trình chính"""
        while True:
            self.hien_thi_menu()
            try:
                lua_chon = input("Nhập lựa chọn của bạn (0-6): ").strip()

                if lua_chon == "0":
                    print("Cảm ơn bạn đã sử dụng chương trình!")
                    break

                elif lua_chon == "1":
                    self.quan_ly_du_lieu.hien_thi_du_lieu()

                elif lua_chon == "2":
                    mon = input("Nhập tên môn học: ").strip()
                    try:
                        diem = float(input("Nhập điểm trung bình: "))
                        if 0 <= diem <= 10:
                            self.quan_ly_du_lieu.them_mon_hoc(mon, diem)
                        else:
                            print("Điểm phải nằm trong khoảng 0-10!")
                    except ValueError:
                        print("Điểm phải là số thực!")

                elif lua_chon == "3":
                    mon = input("Nhập tên môn học cần sửa: ").strip()
                    try:
                        diem_moi = float(input("Nhập điểm mới: "))
                        if 0 <= diem_moi <= 10:
                            self.quan_ly_du_lieu.sua_diem(mon, diem_moi)
                        else:
                            print("Điểm phải nằm trong khoảng 0-10!")
                    except ValueError:
                        print("Điểm phải là số thực!")

                elif lua_chon == "4":
                    mon = input("Nhập tên môn học cần xóa: ").strip()
                    self.quan_ly_du_lieu.xoa_mon_hoc(mon)

                elif lua_chon == "5":
                    print("Đang vẽ biểu đồ cột...")
                    self.ve_bieu_do.ve_bieu_do_cot()

                elif lua_chon == "6":
                    print("Đang vẽ biểu đồ đường...")
                    self.ve_bieu_do.ve_bieu_do_duong()

                else:
                    print("Lựa chọn không hợp lệ! Vui lòng chọn từ 0-6.")

            except KeyboardInterrupt:
                print("\n\nChương trình đã được dừng bởi người dùng.")
                break
            except Exception as e:
                print(f"Có lỗi xảy ra: {e}")

            input("\nNhấn Enter để tiếp tục...")


# ============== CHƯƠNG TRÌNH CHÍNH ==============
if __name__ == "__main__":
    print("Khởi động chương trình...")
    menu = MenuChinh()
    menu.chay_chuong_trinh()
