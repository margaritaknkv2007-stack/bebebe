s = input("Введите числа через пробел:")
num = s.split()
sum = 0
for i in num:
    num = int(i)
    if num % 3 == 0:
        sum += num
print(sum)