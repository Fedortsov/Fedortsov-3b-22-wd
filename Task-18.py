class Figure:

    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter

    def info(self):
        print("площадь", self.square, "периметр", self.perimeter)


figure = Figure(30, 21.9)
figure.info()