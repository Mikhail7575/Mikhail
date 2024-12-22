# 1  Задача с регистром

import random

a = input('Введите имя ')
b = [a.lower(), a.upper()]
random_el = random.choice(b)

print(random_el)
