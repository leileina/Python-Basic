class Product:#Lớp Sản phẩm cơ bản
    def __init__(self, name, price): #Hàm Khởi tạo sản phẩm
        self.name = name 
        self.price = price
        
    def __repr__(self):#Hàm Chuỗi đại diện cho sản phẩm
        return f"{self.__class__.__name__}(name={self.name!r}, price={self.price})"


class Clothing(Product): #Lớp Sản phẩm quần áo
    def __init__(self, name, price, size, color):#Hàm Khởi tạo sản phẩm quần áo
        super().__init__(name, price)
        self.size = size
        self.color = color

    def __repr__(self):#Hàm Chuỗi đại diện cho sản phẩm quần áo
        return f"Clothing(name={self.name!r}, price={self.price}, size={self.size!r}, color={self.color!r})"


class Electronics(Product):#lớp Sản phẩm điện tử
    def __init__(self, name, price, warranty_years, brand):#Hàm Khởi tạo sản phẩm điện tử
        super().__init__(name, price)
        self.warranty_years = warranty_years
        self.brand = brand

    def __repr__(self):#Hàm Chuỗi đại diện cho sản phẩm điện tử
        return (
            f"Electronics(name={self.name!r}, price={self.price}, "
            f"brand={self.brand!r}, warranty_years={self.warranty_years})"
        )


class ProductFactory:#Lớp Nhà máy sản phẩm
    @staticmethod
    def create_product(product_type, **kwargs):#Hàm Tạo sản phẩm dựa trên loại
        t = product_type.strip().lower()
        if t == "clothing":
            return Clothing(
                name=kwargs.get("name"),
                price=kwargs.get("price", 0),
                size=kwargs.get("size", "M"),
                color=kwargs.get("color", "Black"),
            )
        elif t == "electronics":
            return Electronics(
                name=kwargs.get("name"),
                price=kwargs.get("price", 0),
                brand=kwargs.get("brand", "Unknown"),
                warranty_years=kwargs.get("warranty_years", 1),
            )
        else:
            raise ValueError(f"Unsupported product type: {product_type}")


class AppConfig:#Lớp Cấu hình ứng dụng singleton
    _instance = None

    def __new__(cls, **kwargs):#Hàm Tạo instance singleton
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, **kwargs):#Hàm Khởi tạo cấu hình ứng dụng
        if getattr(self, "_initialized", False):
            return
        self.settings = kwargs
        self._initialized = True

    def __repr__(self):#Hàm Chuỗi đại diện cho cấu hình ứng dụng
        return f"AppConfig(settings={self.settings})"


class DatabaseConnection:#Lớp Kết nối cơ sở dữ liệu singleton
    _instance = None

    def __new__(cls, connection_string=None):#Hàm Tạo instance singleton cho kết nối cơ sở dữ liệu
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, connection_string=None):#Hàm Khởi tạo kết nối cơ sở dữ liệu
        if getattr(self, "_initialized", False):
            return
        self.connection_string = connection_string or "sqlite:///:memory:"
        self.connected = False
        self._initialized = True

    def connect(self):#Hàm Kết nối đến cơ sở dữ liệu
        if not self.connected:
            self.connected = True

    def disconnect(self):#Hàm Ngắt kết nối đến cơ sở dữ liệu
        if self.connected:
            self.connected = False

    def __repr__(self):#Hàm Chuỗi đại diện cho kết nối cơ sở dữ liệu
        return (
            f"DatabaseConnection(connection_string={self.connection_string!r}, "
            f"connected={self.connected})"
        )


class ShoppingCart:#Lớp Giỏ hàng với operator overloading
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add_product(self, product):#Hàm Thêm sản phẩm vào giỏ hàng
        self.items.append(product)

    def __add__(self, other):#Hàm Nối giỏ hàng với operator +
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        new_cart = ShoppingCart(owner=f"{self.owner}+{other.owner}")
        new_cart.items = self.items + other.items
        return new_cart

    def __contains__(self, item_name):#Hàm Kiểm tra sản phẩm trong giỏ hàng với operator in
        item_name_norm = item_name.lower() if isinstance(item_name, str) else item_name
        for item in self.items:
            if isinstance(item_name_norm, str) and item.name.lower() == item_name_norm:
                return True
            if item == item_name_norm:
                return True
        return False

    def total(self):#Hàm Tính tổng giá trị giỏ hàng
        return sum(item.price for item in self.items)

    def __repr__(self):#Hàm Chuỗi đại diện cho giỏ hàng
        return f"ShoppingCart(owner={self.owner!r}, items={self.items})"


if __name__ == "__main__":# Kịch bản thử nghiệm
    print("=== Product Factory ===")
    tshirt = ProductFactory.create_product("Clothing", name="T-Shirt", price=15.5, size="L", color="Blue")
    phone = ProductFactory.create_product("Electronics", name="iPhone", price=999.9, brand="Apple", warranty_years=2)
    print(tshirt)
    print(phone)

    print("\n=== Singleton AppConfig/DatabaseConnection ===")
    cfg1 = AppConfig(app_name="SmartCart", version="1.0")
    cfg2 = AppConfig(debug=True)
    print(cfg1)
    print(cfg2)
    print("AppConfig singleton?", cfg1 is cfg2)

    db1 = DatabaseConnection("postgres://localhost")
    db2 = DatabaseConnection("mysql://localhost")
    db1.connect()
    print(db1)
    print(db2)
    print("DatabaseConnection singleton?", db1 is db2)

    print("\n=== ShoppingCart operator overloading ===")
    cart_a = ShoppingCart("Alice")
    cart_a.add_product(tshirt)
    cart_b = ShoppingCart("Bob")
    cart_b.add_product(phone)

    cart_all = cart_a + cart_b
    print(cart_all)
    print("Total:", cart_all.total())
    print("iPhone in cart:", "iPhone" in cart_all)
    print("MacBook in cart:", "MacBook" in cart_all)
