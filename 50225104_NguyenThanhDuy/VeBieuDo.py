import matplotlib.pyplot as plt
class BieuDoCot:
    """Lớp để quản lý và vẽ biểu đồ cột điểm sinh viên"""
    
    def __init__(self, ten_sinh_vien=None, diem=None):
        """
        Hàm khởi tạo
        
        Parameters:
        - ten_sinh_vien: Danh sách tên sinh viên
        - diem: Danh sách điểm sinh viên
        """
        self.ten_sinh_vien = ten_sinh_vien if ten_sinh_vien is not None else []
        self.diem = diem if diem is not None else []
    
    def nhap_du_lieu(self, ten_sinh_vien, diem):
        """
        Phương thức nhập dữ liệu sinh viên
        
        Parameters:
        - ten_sinh_vien: Danh sách tên sinh viên
        - diem: Danh sách điểm sinh viên
        """
        if len(ten_sinh_vien) != len(diem):
            print("Lỗi: Số lượng tên và điểm không khớp!")
            return False
        
        self.ten_sinh_vien = ten_sinh_vien
        self.diem = diem
        print("Dữ liệu đã được nhập thành công!")
        return True
    
    def hien_thi_du_lieu(self):
        """
        Phương thức hiển thị dữ liệu sinh viên
        """
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
        """
        Phương thức vẽ biểu đồ cột
        """
        if not self.ten_sinh_vien or not self.diem:
            print("Không có dữ liệu để vẽ biểu đồ!")
            return
        
        # Tạo hình vẽ
        plt.figure(figsize=(10, 6))
        
        # Vẽ biểu đồ cột
        plt.bar(self.ten_sinh_vien, self.diem, color='steelblue', edgecolor='navy', alpha=0.7)
        
        # Thiết lập tiêu đề và nhãn trục
        plt.title('Biểu Đồ Cột - Điểm Sinh Viên', fontsize=16, fontweight='bold')
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


# ============== CHƯƠNG TRÌNH CHÍNH ==============
if __name__ == "__main__":
    # Tạo đối tượng BieuDoCot
    bieu_do = BieuDoCot()
    
    # Dữ liệu mẫu
    danh_sach_ten = ["Duy", "Bình", "Huỳnh", "Ý", "Kiệt"]
    danh_sach_diem = [8, 7, 9, 6, 10]
    
    # Nhập dữ liệu
    print("=== CHƯƠNG TRÌNH VẼ BIỂU ĐỒ CỘT ĐIỂM SINH VIÊN ===\n")
    bieu_do.nhap_du_lieu(danh_sach_ten, danh_sach_diem)
    
    # Hiển thị dữ liệu
    bieu_do.hien_thi_du_lieu()
    
    # Vẽ biểu đồ
    print("Đang vẽ biểu đồ...")
    bieu_do.ve_bieu_do()
