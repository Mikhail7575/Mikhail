# 1. Дано число n. Создайте список от n до 0.
'''
n = int(input())
new_list = []
for i in range(n, -1, -1):
    new_list.append(i)
print(new_list)
'''

# 2. Добавить слово "пушистый" к каждому имени.

dinozaurs = ["Ти-рекс", "Трицератопс", "Велоцираптор", "Брахиозавр"]
pushistos_dinozaurs = []
a = "Пушистый "
for i in dinozaurs:
    b = a + i
    pushistos_dinozaurs.append(b)
print(pushistos_dinozaurs)
