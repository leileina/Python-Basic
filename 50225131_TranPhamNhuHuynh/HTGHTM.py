#1. CLASS SẢN PHẨM CƠ BẢN
class Product:
    def __init__(self, name, price):
        self.name = name      # lưu tên sản phẩm vào thuộc tính name
        self.price = price    # lưu giá sản phẩm vào thuộc tính price

    def __str__(self):#tính bao gói tại sao dùng 1 gạch,tsao dùng 2 gạch
        return f"{self.name} - {self.price}"  
        # khi dùng print(object) sẽ hiển thị dạng: "tên - giá"


#2. CÁC LOẠI SẢN PHẨM 
class Clothing(Product):  # kế thừa từ class Product
    def __init__(self, name, price, size):
        super().__init__(name, price)  
        # gọi constructor của class cha để gán name và price

        self.size = size  
        # thêm thuộc tính riêng của Clothing là size (kích cỡ)


class Electronics(Product):  # kế thừa từ Product
    def __init__(self, name, price, warranty):
        super().__init__(name, price)  
        # gọi constructor của class cha

        self.warranty = warranty  
        # thêm thuộc tính riêng: thời gian bảo hành


#3. FACTORY PATTERN 
class ProductFactory:
    @staticmethod  # phương thức tĩnh (không cần tạo object vẫn gọi được)
    def create_product(product_type, **kwargs):
        # product_type: loại sản phẩm (string)
        # **kwargs: nhận nhiều tham số dạng key=value

        if product_type == "clothing":  
            # nếu là quần áo
            return Clothing(
                kwargs["name"],     # lấy name từ kwargs
                kwargs["price"],    # lấy price
                kwargs["size"]      # lấy size
            )

        elif product_type == "electronics":  
            # nếu là đồ điện tử
            return Electronics(
                kwargs["name"],     
                kwargs["price"],    
                kwargs["warranty"]  # lấy warranty
            )

        else:
            raise ValueError("Loại sản phẩm không hợp lệ!")  
            # báo lỗi nếu nhập sai loại


#4. SINGLETON PATTERN 
class DatabaseConnection:
    _instance = None  # biến class lưu object duy nhất

    def __new__(cls):
        if cls._instance is None:  
            # nếu chưa có instance nào
            print("Tạo kết nối database mới...")

            cls._instance = super().__new__(cls)  
            # tạo object mới và lưu vào _instance

        return cls._instance  
        # luôn trả về cùng 1 object (singleton)


#5. SHOPPING CART 
class ShoppingCart:
    def __init__(self):
        self.items = []  
        # danh sách chứa các sản phẩm

    def add_product(self, product):
        self.items.append(product)  
        # thêm sản phẩm vào list

    def show_cart(self):
        for item in self.items:  
            # duyệt từng sản phẩm
            print(item)  
            # in ra (sẽ gọi __str__ của Product)

    # ===== OVERLOAD TOÁN TỬ + =====
    def __add__(self, other):
        new_cart = ShoppingCart()  
        # tạo giỏ hàng mới

        new_cart.items = self.items + other.items  
        # nối 2 danh sách sản phẩm lại

        return new_cart  
        # trả về giỏ hàng mới

    # ===== OVERLOAD TOÁN TỬ "in" =====
    def __contains__(self, product_name):
        for item in self.items:  
            # duyệt từng sản phẩm trong giỏ

            if item.name == product_name:  
                # nếu tên sản phẩm trùng
                return True  

        return False  
        # nếu không tìm thấy thì trả về False


# 6.CHẠY CHƯƠNG TRÌNH

# tạo sản phẩm bằng Factory
p1 = ProductFactory.create_product(
    "clothing",      # loại sản phẩm
    name="Áo thun",  # truyền name
    price=150,       # truyền price
    size="M"         # truyền size
)

p2 = ProductFactory.create_product(
    "electronics",   # loại sản phẩm
    name="Vivo",     #truyền name
    price=2000,      # truyền price
    warranty=12      # truyền thời gian bảo hành
)

# tạo giỏ hàng thứ 1
cart1 = ShoppingCart()
cart1.add_product(p1)  # thêm p1 vào giỏ

# tạo giỏ hàng thứ 2
cart2 = ShoppingCart()
cart2.add_product(p2)  # thêm p2 vào giỏ

# ===== TEST TOÁN TỬ + =====
cart3 = cart1 + cart2  
# gọi __add__ → gộp 2 giỏ thành 1

print("Giỏ hàng sau khi cộng:")
cart3.show_cart()  
# in tất cả sản phẩm trong cart3

#TEST TOÁN TỬ in 
if "iPhone" in cart3:  
    # gọi __contains__
    print("Có iPhone trong giỏ hàng!")

# TEST SINGLETON 
db1 = DatabaseConnection()  
# tạo instance đầu tiên

db2 = DatabaseConnection()  
# vẫn trả về instance cũ

print("db1 và db2 là một:", db1 is db2)  
# kiểm tra 2 biến có cùng object không (True)