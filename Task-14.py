class Student:

    def __init__(self, name, lastname, age, speciality):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.speciality = speciality

    def info(self):
        print(self.name, self.lastname, self.age,"года", self.speciality)


student = Student("Николай", "Федорцов", 24, "Веб-разработка")
student.info()