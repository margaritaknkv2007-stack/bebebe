print("Сколько чисел?")
n = int(input())
chisla = []
for i in range(n):
    chisla.append(int(input("Ввведите число:")))
for i in range(n):
    for j in range(i + 1, n):
        if chisla[i] < chisla[j]:
            chisla[i], chisla[j] = chisla[j], chisla[i]
for x in chisla:
    print(x)
