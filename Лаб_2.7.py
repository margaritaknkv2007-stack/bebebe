print("Сколько чисел?")
n = int(input())
chisla = []
for i in range(n):
    chisla.append(int(input("Введите число:")))
chisla = tuple(chisla)
max = 0
for i in range(len(chisla)):
    if chisla[i] > chisla[max]:
        max = i
print("Индекс максимального элемента:", max)