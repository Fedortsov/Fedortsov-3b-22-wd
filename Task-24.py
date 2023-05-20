class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def performance(self):
        print("Имя", self.name,"Возраст", self.age,"лет", "Зарплата", self.salary, "руб.")


employee = Employee('Николай', 24, 40000)
employee.performance()