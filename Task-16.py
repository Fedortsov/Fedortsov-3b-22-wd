class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print("Кошка",self.name, self.age, "лет","цвет", self.color)


my_cat = Cat("Дина", 6, "черно-желто-белая")
my_cat.info()