# 1  Задача с регистром.Смог только через список.

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
    
