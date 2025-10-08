import math
a = float(input("Введите угол в градусах: "))
print("Угол = ", a)

z1 = math.cos(a) + math.cos(2*a) + math.cos(6*a) + math.cos(7*a)
print("При угле a =", a, "z1 =", z1)



