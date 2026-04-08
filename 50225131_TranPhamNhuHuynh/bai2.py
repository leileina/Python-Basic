class Date:
    def __init__(self, ngay, thang, nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    # Kiểm tra năm nhuận
    def la_nam_nhuan(self):
        return (self.nam % 400 == 0) or (self.nam % 4 == 0 and self.nam % 100 != 0)
    
    def so_ngay_trong_thang(self):
        if self.thang in [1,3,5,7,8,10,12]:
            return 31
        elif self.thang in [4,6,9,11]:
            return 30
        elif self.thang == 2:
            if self.la_nam_nhuan():
             return 29
        else:
            return 28
    
    # kiểm tra hợp lệ
    def kiem_tra_hop_le(self):
        if self.thang < 1 or self.thang > 12:
            return False
        if self.ngay < 1 or self.ngay > self.so_ngay_trong_thang():
            return False
        return True

    # Hiển thị
    def hien_thi(self):
        print(f"{self.ngay:02d}/{self.thang:02d}/{self.nam}")

    # Ngày hôm sau
    def ngay_hom_sau(self):
        d = self.ngay + 1
        m = self.thang
        y = self.nam
        return Date(d, m, y)

class SDDate:
    def __init__(self, date):
        self.date = date
    def kiem_tra(self):
        if self.date.kiem_tra_hop_le():
            print("Ngày hợp lệ")
        else:
            print("Ngày không hợp lệ")
    
#test
d = Date(29, 2, 2024)  # năm nhuận

sdd = SDDate(d)
sdd.kiem_tra()

d.hien_thi()

ngay_sau = d.ngay_hom_sau()
print("Ngày hôm sau:")
ngay_sau.hien_thi()
    
