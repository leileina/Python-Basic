class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def calculate_salary(self):
        return 0
    
    def show_info(self):
        print("Tên:", self.name)
        print("Mã:", self.id)

class FullTimeEmployee(Employee):
    def __init__(self, name, id, basic_salary):
        super().__init__(name, id)
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary
    
class PartTimeEmployee(Employee):
    def __init__(self, name, id, working_hours, salary_per_hour):
        super().__init__(name, id)
        self.working_hours = working_hours
        self.salary_per_hour = salary_per_hour

    def calculate_salary(self):
        return self.working_hours * self.salary_per_hour


class SalesEmployee(Employee):
    def __init__(self, name, id, basic_salary, sales, commission_rate):
        super().__init__(name, id)
        self.basic_salary = basic_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_salary(self):
        return self.basic_salary + self.sales * self.commission_rate


# Tạo danh sách nhân viên
employees = [
    FullTimeEmployee("Duy", "NV01", 10000000),
    PartTimeEmployee("Bình", "NV02", 80, 50000),
    SalesEmployee("Huỳnh", "NV03", 7000000, 50000000, 0.05)
]

total_salary = 0
max_salary = 0
best_employee = None

for emp in employees:
    emp.show_info()
    salary = emp.calculate_salary()
    print("Lương:", salary)
    print("-------------------")

    total_salary += salary

    if salary > max_salary:
        max_salary = salary
        best_employee = emp

print("Tổng lương:", total_salary)

print("Nhân viên lương cao nhất:")
best_employee.show_info()
print("Lương:", max_salary)

