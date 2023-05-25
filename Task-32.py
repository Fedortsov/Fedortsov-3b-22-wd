class Schoolboy:
    def __init__(self, name, clas):
        self.name = name
        self.clas = clas

    def school(self):
        print(f"{self.name} учится в {self.clas} классе")


Schoolboy1 = Schoolboy("Никита", 1)

Schoolboy1.school()