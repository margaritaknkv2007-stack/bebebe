# print("Сколько элементов в первом множестве?")
# n = int(input())
# mn1 = set()
# for i in range(n):
#     mn1.add(int(input("Введите элемент:")))
# print("Сколько элементов во втором множестве?")
# m = int(input())
# mn2 = set()
# for i in range(m):
#     mn2.add(int(input("Введите элемент:")))
# vtoroe_v_pervom = True
# for x in mn2:
#     if x not in mn1:
#         vtoroe_v_pervom = False
#         break
# pervoe_v_vtorom = True
# for x in mn1:
#     if x not in mn2:
#         pervoe_v_vtorom = False
#         break
# if pervoe_v_vtorom:
#     print("Первое множество является подмножеством второго")
# elif vtoroe_v_pervom:
#     print("Второе множество является подмножеством первого")
# else:
#     print("Ни одно множество не является подмножеством другого")


print("Сколько элементов в первом множестве?")
n = int(input())
mn1 = set()
for i in range(n):
    mn1.add(int(input("Введите элемент:")))

print("Сколько элементов во втором множестве?")
m = int(input())
mn2 = set()
for i in range(m):
    mn2.add(int(input("Введите элемент:")))

if mn1.issubset(mn2):
    print("Первое множество является подмножеством второго")
elif mn2.issubset(mn1):
    print("Второе множество является подмножеством первого")
else:
    print("Ни одно множество не является подмножеством другого")