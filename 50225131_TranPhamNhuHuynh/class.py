class Animal:
    def sound(self):
        print("Con vật kêu")

class Dog(Animal):
    def sound(self):
        print("gâu gâu")
class Cat(Animal):
    def sound(self):
        super().sound()
        print("meo meo")
class Duck(Animal):
    def sound(self):
        print("cạp cạp")

d1 = Dog()
c2 = Cat()
d2 = Duck()

d1.sound()
c2.sound()
d2.sound()
