class Vehicle:
    def __init__(self,name,distance):
        self.name = name
        self.distance = distance
    
    def calculate_cost(self):
        return 0
    
    def show_info(self):
        print("Phương tiện:", self.name)
        print("Quãng đường:", self.distance)

class Car(Vehicle):
    def __init__(self, name, distance, feul_cost_per_km):
        super().__init__(name, distance)
        self.feul_cost_per_km = feul_cost_per_km

    def calculate_cost(self):
        return self.distance * self.feul_cost_per_km\

class Bus(Vehicle):
    def __init__(self, name, distance, ticket_price, passenger_count):
        super().__init__(name, distance)
        self.ticket_price = ticket_price
        self.passenger_count = passenger_count

    def calculate_cost(self):
        return self.ticket_price * self.passenger_count
    
class Truck(Vehicle):
    def __init__(self, name, distance, cost_per_km, load_factor):
        super().__init__(name, distance)
        self.cost_per_km = cost_per_km
        self.load_factor = load_factor

    def calculate_cost(self):
        return self.distance * self.cost_per_km * self.load_factor


vehicles = [
    Car("Xe hơi", 100, 2000),
    Bus("Xe bus", 50, 10000, 40),
    Truck("Xe tải", 200, 3000, 1.5)
]

vehicles.sort(key=lambda v: v.calculate_cost(), reverse=True)

for v in vehicles:
    v.show_info()
    print("Chi phí:", v.calculate_cost())
    print("----------------")