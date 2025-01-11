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
