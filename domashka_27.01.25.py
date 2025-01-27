#  Сумма чисел от 1 до 100
'''
total = sum(i for i in range(1, 101))
print(f"Сумма чисел от 1 до 100: {total}")


# 2 Вывод символов строки


[print(i) for i in input("Введите строку ")]



#  Таблица умножения: Не нашел способа 

number = int(input())
a = 0
for i in range(1, 11):
    a = number * i

    print(f"{number} x {i} = {a}")



# Перевернуть строку 

string = input('Введите строку ')
result = ''
a = [result + string[i] for i in range(len(string) -1, -1, -1)]
print(''.join(a))



# Полиндром 

a = input('Введите слово ')
b = ''
b = [b + a[i] for i in range(len(a)-1, -1, -1)]
print(''.join(b))
if a == ''.join(b):
    print('Это полиндром')
else:
    print('Это не полиндром')

	

#  Дано число n. Создайте список от n до 0.

import random

n = int(input())
new_list = []
new_list = [i for i in range(n, -1, -1)]
    
print(new_list)



#  Добавить слово "пушистый" к каждому имени.

dinozaurs = ["Ти-рекс", "Трицератопс", "Велоцираптор", "Брахиозавр"]

a = "Пушистый "
pushistos_dinozaurs = ["Пушистый " + i for i in dinozaurs]

print(pushistos_dinozaurs)



# Случайнр выбирает три ингредиента для нового рецепта
import random

ingredients = ["сыр", "яйца", "помидоры", "курица", "рыба", "грибы", "лук"]
new_recept = []
new_recept = [random.choice(ingredients) for i in range(3)]
    
print(new_recept)



names = [("Иванов", "Иван"), ("Петров", "Петров"), ("Сидоров", "Сидор")]
new_names = []
new_names = [i[::-1] for i in names]
    
print(new_names)


#  Сгенерируйте пароль из случайного набора символов длинной 8.
import random
letters = "abcdefghijklmnopqrwxvzABCDEFJHIJKLNMOPQRWXVZ0123456789"
password = ""
password = [random.choice(letters) for i in range(8)]

print(''.join(password))



#  Разделить числа на два списка четные и не четные

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
not_even_numbers = []

even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)

not_even_numbers = [i for i in numbers if i % 2 != 0]    
print(not_even_numbers)


#  Разделите строку,содержащую книгу главу,на отдельные части:
# название книги и номер главы.

text = "Гарри Поттер и Тайная комната - Глава 2"
book_title = ""
chapter_number = ""
book_title = ''.join([i for i in text])
if '-' in book_title:
    book_title = book_title[:book_title.index('-')+1]

chapter_number = ''.join([i for i in text if i.isdigit()])
print(f'Книга: {book_title} Глава: {chapter_number}')

'''
