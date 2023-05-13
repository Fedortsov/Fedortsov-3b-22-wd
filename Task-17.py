class Book:

    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def info(self):
        print(self.title, self.author, self.year, self.genre)


my_favourite_book = Book("Портрет Дориана Грея", "Оскар Уайльд", 1890, "роман")
my_favourite_book.info()