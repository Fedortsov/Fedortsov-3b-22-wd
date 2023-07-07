import sqlite3

conn = sqlite3.connect('database_employees.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees
(id INTEGER PRIMARY KEY, name TEXT, function TEXT, salary REAL)''')

cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('Alex', 'Ученый', 2000))
cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('Margot', 'Менеджер', 900))
cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('John', 'Электрик', 1500))

cursor.execute("SELECT * FROM employees WHERE function = 'Менеджер'")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()

conn.close()