import sqlite3

conn = sqlite3.connect('database_books.db', detect_types=sqlite3.PARSE_DECLTYPES)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books
(id INTEGER PRIMARY KEY, name TEXT, author TEXT, release DATE)''')

cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Долина ужаса', 'Дойл Артур Конан', ' 1915-02-27'))
cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Портрет Дориана Грея', 'Оскар Уайльд', '1891-04-15'))
cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Отцы и дети', 'Тургенев Иван.', '1883-07-21'))

cursor.execute("SELECT * FROM books WHERE DATE(release) > '2000-01-01'")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()

conn.close()