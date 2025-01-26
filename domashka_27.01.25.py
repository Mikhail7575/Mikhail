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

	'''
