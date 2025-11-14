import math
a = float(input("Введите угол в градусах: "))
print("Угол = ", a)
rad = math.radians(a)
z1 = math.cos(rad) + math.cos(2*rad) + math.cos(6*rad) + math.cos(7*rad)
print("При угле a =", a, "z1 =", z1)



