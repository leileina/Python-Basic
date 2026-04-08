
# ===== STRATEGY =====
class ShippingStrategy():
    def calculate_cost(self, weight, distance):
        self.weight = weight
        self.distance = distance

# ===== CÁC CHIẾN LƯỢC =====
class StandardShipping(ShippingStrategy): #=> ghi đè
    def calculate_cost(self, weight, distance): #hàm tính phí ship
        return 10  # đồng giá  
    #Mọi kiểu giao hàng đều phải có cách tính phí riêng


class ExpressShipping(ShippingStrategy):
    def calculate_cost(self, weight, distance):
        return weight * 5  # tính theo cân nặng


class DroneShipping(ShippingStrategy):
    def calculate_cost(self, weight, distance):
        return distance * 2  # tính theo khoảng cách


# ===== ORDER =====
class Order:
    def __init__(self, strategy):
        self.strategy = strategy  # nhận strategy

    def calculate_shipping(self, weight, distance):
        return self.strategy.calculate_cost(weight, distance)
    
# ===== TEST =====
def main():
    # tạo đơn hàng với từng chiến lược

    order1 = Order(StandardShipping())
    print("Standard:", order1.calculate_shipping(10, 50))

    order2 = Order(ExpressShipping())
    print("Express:", order2.calculate_shipping(10, 50))

    order3 = Order(DroneShipping())
    print("Drone:", order3.calculate_shipping(10, 50))


# gọi hàm main để chạy
main()