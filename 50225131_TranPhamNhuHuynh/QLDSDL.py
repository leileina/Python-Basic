# Lớp cha 1
class Destination:
    def __init__(self, destination):
        self.destination = destination


# Lớp cha 2
class Transport:
    def __init__(self, transport):
        self.transport = transport


# Lớp cha 3
class Cost:
    def __init__(self, cost):
        self.cost = cost


# Lớp con
class Tour(Destination, Transport, Cost):
    def __init__(self, ma_tour, so_ngay, cong_ty, destination, transport, cost):
        Destination.__init__(self, destination)
        Transport.__init__(self, transport)
        Cost.__init__(self, cost)

        self.ma_tour = ma_tour
        self.so_ngay = so_ngay
        self.cong_ty = cong_ty

    def show_info(self):
        print("Mã tour:", self.ma_tour,
              "| Điểm đến:", self.destination,
              "| Phương tiện:", self.transport,
              "| Chi phí:", self.cost,
              "| Số ngày:", self.so_ngay,
              "| Công ty:", self.cong_ty)


# ===== Chương trình chính =====
tours = []

n = int(input("Nhập số lượng tour: "))

for i in range(n):
    print("\nNhập tour", i+1)
    ma = input("Mã tour: ")
    des = input("Điểm đến: ")
    tran = input("Phương tiện: ")
    cost = float(input("Chi phí: "))
    day = int(input("Số ngày: "))
    company = input("Công ty tổ chức: ")

    t = Tour(ma, day, company, des, tran, cost)
    tours.append(t)


# In danh sách
print("\nDanh sách tour:")
for t in tours:
    t.show_info()


# Sắp xếp theo chi phí tăng dần
tours.sort(key=lambda x: x.cost)
print("\nDanh sách sau khi sắp xếp theo chi phí tăng dần:")
for t in tours:
    t.show_info()


# Sắp xếp theo số ngày giảm dần
tours.sort(key=lambda x: x.so_ngay, reverse=True)
print("\nDanh sách sau khi sắp xếp theo số ngày giảm dần:")
for t in tours:
    t.show_info()


# Tìm tour đắt nhất
max_tour = max(tours, key=lambda x: x.cost)
print("\nTour đắt nhất:")
max_tour.show_info()


# Tìm tour ngắn ngày nhất
min_day = min(tours, key=lambda x: x.so_ngay)
print("\nTour ngắn ngày nhất:")
min_day.show_info()


# Lọc theo phương tiện
pt = input("\nNhập phương tiện cần tìm: ")
print("Các tour dùng phương tiện", pt)
for t in tours:
    if t.transport.lower() == pt.lower():
        t.show_info()


# Đếm số tour theo công ty
company = input("\nNhập công ty cần đếm: ")
count = 0
for t in tours:
    if t.cong_ty.lower() == company.lower():
        count += 1
print("Số tour của công ty", company, ":", count)


# Tính chi phí trung bình
total = sum(t.cost for t in tours)
avg = total / len(tours)
print("\nChi phí trung bình:", avg)


# Tìm theo mã tour
ma = input("\nNhập mã tour cần tìm: ")
for t in tours:
    if t.ma_tour == ma:
        print("Tour tìm được:")
        t.show_info()


# Lọc tour từ 3 ngày trở lên
print("\nTour từ 3 ngày trở lên:")
for t in tours:
    if t.so_ngay >= 3:
        t.show_info()


# Lọc tour theo mức chi phí
gia = float(input("\nNhập mức chi phí tối đa: "))
print("Các tour có chi phí <= ", gia)
for t in tours:
    if t.cost <= gia:
        t.show_info()
