class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.bred = breed

    def about_dog(self):
        print("Собака", self.name,','" порода", self.bred,','" возраст", self.age)


dog = Dog("Шарик","дворняга", 5)
dog.about_dog()