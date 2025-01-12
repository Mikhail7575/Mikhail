# 1. Дано число n. Создайте список от n до 0.

import random

n = int(input())
new_list = []
for i in range(n, -1, -1):
    new_list.append(i)
print(new_list)


# 2. Добавить слово "пушистый" к каждому имени.

dinozaurs = ["Ти-рекс", "Трицератопс", "Велоцираптор", "Брахиозавр"]
pushistos_dinozaurs = []
a = "Пушистый "
for i in dinozaurs:
    b = a + i
    pushistos_dinozaurs.append(b)
print(pushistos_dinozaurs)


# 3. Случайнр выбирает три ингредиента для нового рецепта


ingredients = ["сыр", "яйца", "помидоры", "курица", "рыба", "грибы", "лук"]
new_recept = []
for i in range(3):
    b = random.choice(ingredients)
    new_recept.append(b)
print(new_recept)


# 4. Поменять местами имя и фамилию в каждом кортеже.

names = [("Иванов", "Иван"), ("Петров", "Петров"), ("Сидоров", "Сидор")]
new_names = []
for i in names:
    a = i[::-1]
    new_names.append(a)
print(new_names)


# 5. Сгенерируйте пароль из случайного набора символов длинной 8.

letters = "abcdefghijklmnopqrwxvzABCDEFJHIJKLNMOPQRWXVZ0123456789"
password = ""
for i in range(8):
    a = random.choice(letters)
    password += a
print(password)


# 6. Разделить числа на два списка четные и не четные

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
not_even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        not_even_numbers.append(i)
print(even_numbers)
print(not_even_numbers)


# 7. Разделите строку,содержащую книгу главу,на отдельные части:
# название книги и номер главы.

text = "Гарри Поттер и Тайная комната - Глава 2"
book_title = ""
chapter_number = ""
for i in text:
    book_title += i
    if i == "-":
        break
book_title = book_title.rstrip('-')
for i in text:
    if i.isdigit():
        chapter_number += i
        print(f'Книга: {book_title}, Глава: {chapter_number}')


# 8. Выбирите случайное прздравление из списка,не включая те,которые
# содержат слово "скучный".


greetings = ["C днем рождения!", "С новым годом!",
             "Желаю успехов!", "Скучный текст"]
a = "Скучный"
new_greetings = []

for i in greetings:
    if a not in i:
        new_greetings.append(i)
    else:
        pass
for i in range(1):
    b = random.choice(new_greetings)
print(b)


# 9. Замените все не приличные слова в тексте звездочками.

text = "Эта программа такая тупая! Вот блин!"
new_text = []
a = 'тупая!'
b = 'блин!'
text = text.split(' ')
for i in text:
    new_text.append(i)
    if i == a or i == b:
        new_text.remove(i)
        i = i.rstrip('!')
        i = ('*' * len(i))
        i += '!'
        new_text.append(i)
new_text = ' '.join(new_text)
print(new_text)
