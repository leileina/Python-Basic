class Vehicle:
    def move(self):
        print("Phương tiện đang di chuyển")

# Lớp con Car
class Car(Vehicle):
    def move(self):
        print("Xe chạy trên đường")

# Lớp con Boat
class Boat(Vehicle):
    def move(self):
        print("Thuyền chạy trên nước")

# Lớp con Plane
class Plane(Vehicle):
    def move(self):
        print("Máy bay bay trên trời")


# Tạo danh sách các phương tiện
vehicles = [Car(), Boat(), Plane()]

# Dùng vòng lặp gọi move()
for v in vehicles:
    v.move() 