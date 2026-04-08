#Bài 2: Lớp Date (Ngày tháng)
#Thuộc tính: ngay, thang, nam.
#Phương thức: kiem_tra_hop_le(), hien_thi(), ngay_hom_sau().
#Lớp SDDate: Kiểm tra tính đúng đắn của các ngày đặc biệt (như 29/2 năm nhuận).

# Tạo một lớp (class) tên là Date để quản lý ngày tháng năm.
class Date:
# Hàm khởi tạo
    def __init__(self, ngay, thang, nam):
# Gán giá trị cho thuộc tính
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

# Kiểm tra có phải năm nhuận ko
# Điều kiện:Chia hết cho 4 => năm nhuận
# Không chia hết cho 100 => ko phải năm nhuận
# HOẶC chia hết cho 400 => năm nhuận
    def la_nam_nhuan(self):
        return (self.nam % 4 == 0 and self.nam % 100 != 0) or (self.nam % 400 == 0)
    
# Trả về số ngày của tháng hiện tại
    def so_ngay_trong_thang(self):
# các thang cs 31 ngày
        if self.thang in [1, 3, 5, 7, 8, 10, 12]:
            return 31
# cac tháng cs 30 ngày
        elif self.thang in [4, 6, 9, 11]:
            return 30
        elif self.thang == 2:
            return 29 if self.la_nam_nhuan() else 28
        return 0

# Kiểm tra hợp lệ
#👉 Kiểm tra:

#Tháng phải từ 1 → 12
#Ngày phải nằm trong số ngày của tháng

#Ví dụ:
#31/2 →  sai
#29/2/2024 →  đúng
    def kiem_tra_hop_le(self):
        if self.thang < 1 or self.thang > 12:
            return False
        if self.ngay < 1 or self.ngay > self.so_ngay_trong_thang():
            return False
        return True

#hiển thị
    def hien_thi(self):
#self.ngay → giá trị ngày 
#d → kiểu số nguyên (integer)
#02 → luôn hiển thị 2 chữ số

#Nếu thiếu số → thêm số 0 phía trước
        print("{self.ngay:02d}/{self.thang:02d}/{self.nam}")

# Tính ngày hôm sau
    def ngay_hom_sau(self):
# Tăng lên 1
        self.ngay += 1
#nếu vượt số ngày trong tháng
        if self.ngay > self.so_ngay_trong_thang():
# sang tháng ms
            self.ngay = 1
            self.thang += 1
            if self.thang > 12:
                self.thang = 1
                self.nam += 1


class SDDate():
    def __init__(self):
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        
        self.date = Date(ngay, thang, nam)

    def run(self):
        if self.date.kiem_tra_hop_le():
            print("Ngày hợp lệ:")
            self.date.hien_thi()

            print("Ngày hôm sau là:")
            self.date.ngay_hom_sau()
            self.date.hien_thi()
        else:
            print("Ngày không hợp lệ!")

#Tạo chương trình và chạy 
if __name__ == "__main__":
    app = SDDate()
    app.run()