class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_me(self):
        print("Имя", self.name, "Возраст", self.age)


Person1 = Person("Николай", 24)

Person1.about_me()