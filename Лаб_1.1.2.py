import math
a = float(input("Введите угол в градусах: "))
print("Угол = ", a)
a_rad = math.radians(a)
z2 = 4*math.cos(a_rad/2) * math.cos(5*a_rad/2) * math.cos(4*a_rad)
print("При угле a =", a, "z2 =", z2)



