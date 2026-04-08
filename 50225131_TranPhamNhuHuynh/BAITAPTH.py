class Brand:
    def __init__(self, brand):
        self.brand = brand

class Screen:
    def __init__(self, screen):
        self.screen = screen

class Battery:
    def __init__(self, battery):
        self.battery = battery

class Phone:
    def __init__(self, brand, screen, battery, phone_name, price, color):
        Brand.__init__(self, brand)
        Screen.__init__(self, screen)
        Battery.__init__(self, battery)

        # Thuộc tính riêng của Phone
        self.phone_name = phone_name
        self.price = price
        self.color = color

# Hàm hiển thị thông tin
    def show_info(self):
        print("Tên điện thoại:", self.phone_name)
        print("Hãng:", self.brand)
        print("Kích thước màn hình:", self.screen)
        print("Dung lượng pin:", self.battery)
        print("Màu sắc:", self.color)
        print("Giá bán:", self.price)
        print("Điện thoại", self.phone_name, "thuộc hãng", self.brand)
        print()

# ====== Nhập dữ liệu điện thoại 1 ======
print("Nhập thông tin điện thoại 1")

brand = input("Nhập hãng: ")
screen = input("Nhập kích thước màn hình: ")
battery = input("Nhập dung lượng pin: ")
name = input("Nhập tên điện thoại: ")
price = input("Nhập giá bán: ")
color = input("Nhập màu sắc: ")

phone1 = Phone(brand, screen, battery, name, price, color)

 # ====== Nhập dữ liệu điện thoại 2 ======
brand = input("Nhập hãng: ")
screen = input("Nhập kích thước màn hình: ")
battery = input("Nhập dung lượng pin: ")
phone_name = input("Nhập tên điện thoại: ")
price = input("Nhập giá bán: ")
color = input("Nhập màu: ")

phone2 = Phone(brand, screen, battery, phone_name, price, color)

# ====== In thông tin ======
phone1.show_info()
phone2.show_info()


        
