nam = int(input("Введите число: "))
counter = 0
for i in range(2, nam // 2+1):
    if (nam % i == 0):
        counter = counter+1
if (counter <= 0):
    print("Число простое")
else:
    print("Число не является простым")

