# 1 Программа сравнивает какое число больше 

a = int(input('Введите 1-е число '))
b = int(input('Введите 2-е число '))
if a > b:
    print(a, 'больше', b)
elif a < b:
    print(a, 'меньше', b) 
else:
    print('числа равны')