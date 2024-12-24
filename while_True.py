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
