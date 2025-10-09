num = int(input("Вседите число:"))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print("Сумма цифр данного числа равна:", sum)