from random import randint
# Задание №1
array = []
for i in range(3):
    array.append(randint(0, 100))
average_value = (array[0] + array[1] + array[2])/3
print(average_value)
# Задание №2
x = randint(100, 1000)
y = randint(0, 100)
print(x, y)
print("Результат целочисленного деления:", x // y)
print("Остаток от деления:", x % y)
# Задание №3
number = 125.5673
print(round(number, 2))
print(round(number))
print('{0:011}'.format(number))