#Bài 1: Lớp Diem (Điểm 2D)
#Thuộc tính: x, y.
#Phương thức: nhap_diem(), hien_thi(), doi_diem(dx, dy), tinh_khoang_cach().
#Lớp SDDiem: Tạo điểm $A(3,4)$, điểm $B$ nhập từ bàn phím, điểm $C$ đối xứng với $B$ qua gốc tọa độ. Tính khoảng cách $AB$
import math #Dùng để gọi hàm math.sqrt() (tính căn bậc 2)
class Diem:
    def __init__(self, x=0, y=0): #Tạo lớp biểu diễn 1 điểm (x, y)
        self.x = x#hoành
        self.y = y#tung
    def nhap_diem(self):
        self.x = float(input("Nhập x: "))
        self.y = float(input("Nhập y: "))

    def hien_thi(self):
        print("self.x","self.y")

    def doi_diem(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def tinh_khoang_cach(self, d):
        ###CÔNG THỨC TÍNH KHOẢNG CÁCH###
        return math.sqrt ((self.x - d.x)**2 + (self.y - d.y)**2)

class SDDiem:
    def SSDiem(self, SSDiem):
        self.SSDiem = SSDiem

A = Diem(3, 4)

print("Nhập điểm B:")
B = Diem()
B.nhap_diem()

# Điểm C đối xứng qua gốc
C = Diem(-B.x, -B.y)

print("Điểm A:  ")
A.hien_thi()

print("Điểm B: ")
B.hien_thi()

print("Điểm C:")
C.hien_thi()

print("Khoảng cách AB:", A.tinh_khoang_cach(B))