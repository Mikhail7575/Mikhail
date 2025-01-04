parol = 'Lemmy'

while True:
    a = input(' enter password ')
    if parol == a:
        print('password is true')
        break


#1 Сумма чисел от 1 до 100

total = 0

for i in range(1,101):
    total += i
print(total)

#2 Вывод символов строки

string = input()
for i in string:
    print(i)
 
 
#3 Таблица умножения
number = int(input())

for i in range(1,11):
    print(i * number)


#4 Сумма четных чисел

n = int(input())
a = 0
for i in range(0, n+1, 2):
    a = a + i
print(f"Сумма четных чисел от {1} до {n} = {a}") 


#5 Сумма чисел кратных 3

summa = 0
result = 0
n = int(input('Введите число '))
while summa < n:
    summa += 3
    result = result + summa
print(f"Сумма чисел, кратных 3, от 1 до {n} = {result}")

#6 Простое число
# Я бы сам никогда не додумался-загуглил!
# Но все равно не понимаю!

n = int(input('Введите число '))
k = 0
for i in range(2, n // 2 + 1 ):
    if n % i == 0:
        k = k + 1
if k <= 0:        
    print('Число простое')
else:
    print('Число сложное')
        

#7 факториал числа

n = int(input('Введите число '))
factorial = 1
b = 0
while b < n:
    b += 1
    factorial = factorial * b
print(f"Факториал числа {n} = {factorial}")




#8 Перевернуть строку 
# Сам бы тоже не решил. 
# Тоже не понимаю...Зачем например в range 3-й  (-1) ?

string = input('Введите строку ')
result = ''
for i in range(len(string) -1, -1, -1):
    result += string[i]
print(result)        


#9 угадать число

import random

a = random.randint(1, 101)

#print(a) # Проверял как работает программа

guest = int(input('Введите число '))

for i in range(1,11):
    if guest == (a + i) or guest == (a - i):
        print('Горячо!')
    else:
        pass
if guest > (a + 11):
    print('Ваше число больше')
elif guest < (a - 11):
    print('Ваше число меньше')
elif guest == a:
    print('Вы выйграли')
else:
    pass

 
#10 Полиндром 

a = input('Введите слово ')
b = ''
for i in range(len(a)-1, -1, -1):
    b += a[i]
    print(b)
if a == b:
    print('Это полиндром')
else:
    print('Это не полиндром')

    