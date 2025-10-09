stroka = input("Введите строку:")
razlichnye = ""
for simvol in stroka:
    if simvol not in razlichnye:
        razlichnye += simvol
print(len(razlichnye))