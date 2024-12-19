# 1 Программа сравнивает какое число больше 

a = int(input('Введите 1-е число '))
b = int(input('Введите 2-е число '))
if a > b:
    print("а больше b")
elif a < b:
    print("a меньше b") 
else:
    print("числа равны")

# 2 Программа определяет какое число четное

a = int(input("Введите число"))
if a / 2:
    print('Число четное')
else:
    print('Число не четное')


# 3 Программа определяет положительное или отрицательное число

a = int(input("Введите число "))
if a > 0:
    print('Число положительное') 
elif a < 0:
    print("Число отрицательное") 
else:
    print("Число равно нулю")  

#4 Калькулятор

a = int(input('Введите 1-е число '))
operation = input("Введите арифметическое действие")
b = int(input('Введите 2-e число '))

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
else operation == '/':
    if a or b == 0:
        print('Такой операции нет') 
    print(a / b)
                 
#5 
      

           