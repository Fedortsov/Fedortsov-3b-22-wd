class Recttangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def square(self):
        print("Площадь прямоугольника", self.width * self.length)

Recttangle1 = Recttangle(20, 30)

Recttangle1.square()