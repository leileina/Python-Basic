class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = 0
        self.set_price(price)

# cập nhật giá
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Giá phải lớn hơn 0")

    # xem giá
    def get_price(self):
        return self.__price


# Lớp con kế thừa
class DiscountProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    # tính giá sau giảm
    def final_price(self):
        price = self.get_price()
        return price - (price * self.discount / 100)


# Tạo sản phẩm giảm giá
sp = DiscountProduct("Laptop", 20000000, 10)

# Cập nhật giá
sp.set_price(18000000)

# In giá
print("Tên sản phẩm:", sp.name)
print("Giá gốc:", sp.get_price())
print("Giá sau giảm:", sp.final_price())
