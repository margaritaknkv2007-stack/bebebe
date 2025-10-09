
strochki = []
print("Вводите строки:")
while True:
    strochka = input()
    if strochka == "": 
        break
    strochki.append(strochka)
for strochka in strochki:
    if strochka[0].isupper():
        print(strochka)