 # Какое время суток

time = int(input('Введите время от 0 до 23 '))

if time >= 6 and time <= 11:
    print('Утро')
elif time >= 12 and time <= 18:
    print('День')
elif time >= 18 and time <= 23:
    print('Вечер')
else:
    print('Ночь')