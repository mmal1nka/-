# Задание №1
x = int(input("Введите число: "))
if (x % 5 == 0) and (x % 3 == 0):
    print("Fizz Buzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print(x)
# Задание №2
x = int(input("Введите число: "))
if x % 2 != 0:
    print("Плохо")
elif (x >= 2) and (x <= 5):
    print("Неплохо")
elif (x >= 6) and (x <= 20):
    print("Так себе")
else:
    if x > 20:
        print("Отлично")
    else:
        print("Число не подошло ни под одно правило")
# Задание №3
from random import randint

N = randint(1, 9)
# print(N)
for i in range(N):
    print(i + 1)
# Задание №4
text = "How are you? Eh, ok. Low or Lower? Ohhh."
text_2 = ""
for i in range(len(text)):
    if (text[i].isupper() == True):
        text_2 += text[i]
print(text_2)
# Задание №5
text1 = 'Hello World hello'
text2 = 'He is 123 man'
text3 = '1 2 3 4'


def check(text):
    count = 0
    for word in text.split():
        if word.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False


print(check(text1))
print(check(text2))
print(check(text3))
# Задание №6
array1 = ["left", "right", "left", "stop"]
array2 = ["bright aright", "ok"]
array3 = ["enough", "jokes"]


def left(text):
    string = ''
    for i in range(len(text)):
        string += text[i] + ','
    string = string.rstrip(string[-1])
    new_text = string.replace('right', 'left')
    return (new_text)


print(left(array1))
print(left(array2))
print(left(array3))
