class Student:

    def __init__(self, name, lastname, group, grades):
        self.name = name
        self.lastname = lastname
        self.group = group
        self.grades = grades

    def gpa(self):
        print(sum(self.grades) / len(self.grades))


student = Student("Николай", "Федорцов", "OD-22-WD", [5, 5, 3])
student.gpa()