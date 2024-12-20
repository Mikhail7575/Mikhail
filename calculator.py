a = int(input('Введите 1-е число '))
operation = input("Введите арифметическое действие ")
b = int(input('Введите 2-e число '))

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
else:
    if a == 0 or b == 0:
        print('Такой операции нет')
    else:
        print(a / b)     
    