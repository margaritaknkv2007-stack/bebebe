num = int(input("Введите число:"))
if num < 2:
    print("NO")
else:
    x = True
    for i in range(2, num):
        if num % i == 0:
            x = False
            break
    if x:
        print("YES")
    else:
        print("NO")