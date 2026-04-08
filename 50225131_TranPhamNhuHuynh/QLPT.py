class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_Vehicle_info(self):
        print("Hãng xe:", self.brand)
        print("Năm sản xuất:", self.year)

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)
        self.__speed = 0 #thuộc tinh private

    def set_speed(self, speed):
        if speed >= 0:
          self.__speed = speed
        else:
            print("Vận tốc không hợp lệ!:")

    def get_speed(self):
        return self.__speed
    
    def show_Car_info(self):
        self.show_Vehicle_info()
        print("Vận tốc:", self.__speed)

car1 = Car("Toyota", 2025)
car1.set_speed(80)
car1.show_Car_info()