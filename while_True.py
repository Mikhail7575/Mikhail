parol = 'Lemmy'

while True:
    a = input(' enter password ')
    if parol == a:

    print('password is true')
        break

total = 0

#1

for i in range(1,101):
    total += i
print(total)

#2

string = input()
for i in string:
    print(i)

#3
number = int(input())

for i in range(1,16):
    print(i * number)

#4
n = int(input())
for i in range(0, n, 2):
    print(n + i)    


#5

summa = 0
result = 0
n = int(input('Введите число '))
while summa < n:
    summa += 3
    result = result + summa
print(result)

#6 Я бы сам никогда не додумался-загуглил!
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
        
    