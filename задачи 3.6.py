#Задание №1
name = input("Write your name: ")
last_name = input("Write your surname: ")
print(f"Hello, {name} {last_name}! You just delved into Python. Great start!")
#Задание №2
thickness = 5
c = 'L'
for i in range(thickness+1):
    print((c*(thickness+1)).center(thickness*2))
for i in range(thickness+1):
    print((c*(thickness+1)).center(thickness*2))
for i in range(thickness-2):
    print((c*thickness*5).center(thickness*6))
#Задание №3
text = "ТУСУР - университет мира!"
print(text.title())
#Задание №4
amount = 112543.746
print('{0:,.2f}'.format(amount))
#Задание №5
height = 11
width = height * 3
for stick_count in range(1, height, 2):
    print(('/%/' * stick_count).center(width, '*'))
print(''.center(width, ':'))
for stick_count in range(height-2, 0, -2):
    print(('/%/' * stick_count).center(width, '*'))
