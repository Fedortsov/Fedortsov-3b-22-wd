f1 = 1
f2 = 1

n = int(input("Количество чисел ряда Фибоначчи: "))

print(f1, f2, end=" ")

while n > 2:
    f1, f2 = f2, f1 + f2
    print(f2, end=" ")
    n -= 1