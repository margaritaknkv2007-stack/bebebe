students = {}
n = int(input("Сколько студентов? "))

for i in range(n):
    name = input("Имя: ")
    age = int(input("Возраст: "))
    students[name] = age

max_age = 0
oldest_student = ""

for name in students.keys():
    age = students[name]
    if age > max_age:
        max_age = age
        oldest_student = name

print("Самый старший:", oldest_student)