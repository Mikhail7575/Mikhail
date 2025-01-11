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
