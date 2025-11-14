s = input("Введите числа через пробел:")
num = s.split()
sum = 0
for i in num:
    try:
        num = int(i)
        if num % 3 == 0:
            sum += num
    except ValueError:
        print("Ошибка: '{i}' не является числом")
print(sum)