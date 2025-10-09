# Вводим список строк с клавиатуры
stroki = []
print("Введите строки (пустая строка - конец):")

while True:
    s = input()
    if s == "":
        break
    stroki.append(s)

# Вводим слово для поиска
slovo = input("Введите слово для поиска: ")

# Проверяем в каждой строке
nashlos = False
for stroka in stroki:
    if slovo in stroka:
        nashlos = True
        break

if nashlos:
    print("Да, такое слово есть")
else:
    print("Нет, такого слова нет")