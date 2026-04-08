class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_Person_info(self):
        print("Họ tên:", self.name)
        print("Tuổi:", self.age)

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__score = 0 #thuộc tính private
    def set_score(self, score):
        if 0 <= score <= 10:
            self.__score = score
        else:
            print("Điểm không hợp lệ(0 - 10)")

    def get_score(self):
        return self.__score
    
    def show_student_info(self):
        print("Họ tên:", self.name)
        print("Tuổi:", self.age)
        print("Điểm trung bình:", self.__score)

        
###### chạy chương trình
name = input("Nhập họ tên: ")
age = int(input("Nhập tuổi: "))
score = float(input("Nhập điểm trung bình: "))

hs = Student(name, age)   # tạo học sinh
hs.set_score(score)       # gán điểm

print("\nThông tin học sinh:")
hs.show_student_info()

        
                
