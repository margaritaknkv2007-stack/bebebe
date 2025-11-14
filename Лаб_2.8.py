print("Сколько чисел?")
n = int(input())
chisla = []
for i in range(n):
    chisla.append(int(input("Введите число:")))

chisla.sort(reverse=True)

for x in chisla:
    print(x)