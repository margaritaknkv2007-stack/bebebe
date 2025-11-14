strings_list = []

print("Введите строки для списка:")
while True:
    line = input()
    if line == "":
        break
    strings_list.append(line)

search_word = input("Введите слово для поиска: ")

found = False
for string in strings_list:
    if search_word in string:
        found = True
        break

if found:
    print("Слово найдено")
else:
    print("Слово не найдено")
