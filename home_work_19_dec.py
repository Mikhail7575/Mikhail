# 1  Задача с регистром. Смог только через список.

import random

a = input('Введите имя ')
b = [a.lower(), a.upper()]
random_el = random.choice(b)

print(random_el)

# 2  Длинна слов. 

word_1 = input('Введите 1-е слово ')
word_2 = input('Введите 2-е слово ')

if len(word_1) == len(word_2):
    print('Слова одинаковой длинны')
elif len(word_1) < len(word_2):
    print('Первое слово короче чем второе')
else:
    print('Первое слово длиннее чем второе')


# 3  Бросок кубика  

import random

a = input('Здравствуйте! Как вас зовут? ')
print('Ok ',a,' бросайте кубик... ')

brosok = int(input())

computer =random.randint(1,6)

if brosok > computer:
    print(a, 'Вы выйграли')
elif brosok < computer:
    print(a, 'Вы проиграли')
else:
    print('Ничья', a)


# 4 Проверка треугольника    

a = int(input('Введите длинну 1-ой стороны '))
b = int(input('Введите длинну 2-ой стороны '))
c = int(input('Введите длинну 3-eй стороны '))

if a + b > c and a + c > b and b + c > a:
    print('Это треугольник')
else:
    print('Это не треугольник') 

# Не могу понять,почему не работает так?:
  
a = int(input('Введите длинну 1-ой стороны '))
b = int(input('Введите длинну 2-ой стороны '))
c = int(input('Введите длинну 3-eй стороны ')) 

if a + b > c:
    print('Это треугольник')
elif a + c > c:
    print('Это треугольник')
elif b + c > a:
    print('Это треугольник')    
else:
    print('Это не треугольник') 


# 5  Определение четверти не плоскости

x = int(input('Введите координату х '))
y = int(input('Введите координату y '))

if x > 0 and y > 0:
    print('Точка находится в 1-й четверти')
elif x < 0 and y > 0:
    print('Точка находится в 2-й четверти  ')
elif x < 0 and y < 0:
    print('Точка находится в 3-й четверти')
elif x == 0 and y == 0:
    print('Точка в центре координат')
elif x == 0 and y > 0:
    print('Точка находится на оси y')
elif x == 0 and y < 0:
    print('Точка находится на оси -y')
elif x > 0 and y == 0:
    print('Точка находится на оси x')
elif x < 0 and y == 0:
    print('Точка находится на оси -x')
else:
    print('Точка находится в 4-й четверти ')
