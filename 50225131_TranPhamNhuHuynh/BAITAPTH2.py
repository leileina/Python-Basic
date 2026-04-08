# ===== Lớp cha =====
class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name


class Battery:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity


class Price:
    def __init__(self, price):
        self.price = price


# ===== Lớp con =====
class Phone(Brand, Battery, Price):
    def __init__(self, brand_name, battery_capacity, price, phone_name, color):
        
        # gọi hàm khởi tạo lớp cha
        Brand.__init__(self, brand_name)
        Battery.__init__(self, battery_capacity)
        Price.__init__(self, price)

        # thuộc tính riêng
        self.phone_name = phone_name
        self.color = color

    # hàm hiển thị thông tin
    def show_info(self):
        print("Tên điện thoại:", self.phone_name)
        print("Hãng:", self.brand_name)
        print("Dung lượng pin:", self.battery_capacity)
        print("Màu sắc:", self.color)
        print("Giá:", self.price)
        print("-------------------------")


# ===== Nhập danh sách điện thoại =====
phone_list = []

n = int(input("Nhập số lượng điện thoại: "))

for i in range(n):
    print("\nNhập thông tin điện thoại", i+1)

    brand = input("Hãng: ")
    battery = input("Dung lượng pin: ")
    price = float(input("Giá: "))
    name = input("Tên điện thoại: ")
    color = input("Màu sắc: ")

    phone = Phone(brand, battery, price, name, color)

    phone_list.append(phone)


# ===== In danh sách =====
print("\n===== DANH SÁCH ĐIỆN THOẠI =====")

for p in phone_list:
    p.show_info()


# ===== Sắp xếp theo giá tăng dần =====
phone_list.sort(key=lambda x: x.price)

print("\n===== SẮP XẾP THEO GIÁ TĂNG DẦN =====")

for p in phone_list:
    p.show_info()


# ===== Sắp xếp theo tên điện thoại =====
phone_list.sort(key=lambda x: x.phone_name)

print("\n===== SẮP XẾP THEO TÊN ĐIỆN THOẠI =====")

for p in phone_list:
    p.show_info()