# 1. Увеличение глобальной переменной
# Программа отслеживает общее количество клиентов. Напишите функцию, которая увеличивает #глобальный счётчик клиентов.
# Задача
'''
clients = 0


def add_client():
    global clients
    clients += 1
    pass


add_client()
add_client()
print(clients)



# 2. Изменение цены с локальной и глобальной переменной
# Есть глобальная переменная с базовой ценой товара. Напишите функцию, которая временно изменяет цену локально.
# Задача
base_price = 100


def apply_discount(discount):
    # Локально измените базовую цену, применив скидку
    new_price = (base_price - 20)
    # Локально посчитайте цену со скидкой
    print(f"Цена со скидкой: {new_price}")


apply_discount(20)  # Цена со скидкой: 80
print(base_price)   # Ожидаемый результат: 100



# 3. Применение налогов через map
# Список цен товаров. Напишите функцию, которая добавляет к каждому товару налог 20%, и примените её с помощью map.
# Задача



prices = [100, 200, 300, 400]


def apply_tax(price):
    return price + price * 20 / 100  # Верните цену с налогом 20%


final_prices = list(map(apply_tax, prices))
print(final_prices)

#4. Фильтр товаров по цене
#Есть список цен. Используйте filter, чтобы оставить только товары дороже 150.
# Задача
prices = [50, 120, 180, 300, 75]

# Используйте filter, чтобы отобрать только товары дороже 150
expensive_items = filter(lambda x:x > 150, prices) 
print(list(expensive_items))       # Ожидаемый результат: [180, 300]




# 5. Применение скидки к категории товаров
# У вас есть список цен и категория, к которой нужно применить скидку. Напишите функцию,
# которая с помощью map применяет скидку 10% к заданным категориям.
# Задача
products = [
    {"name": "Laptop", "price": 1000, "category": "electronics"},
    {"name": "Shirt", "price": 50, "category": "clothing"},
    {"name": "Phone", "price": 600, "category": "electronics"},
]


def apply_discount(product):
    if product["category"] == "electronics":
        product["price"] = product["price"] - product["price"] * 10 / 100
    return product


discounted_products = map(apply_discount, products)
print(list(discounted_products))  # Как вывести,чтобы было так же красиво,как products ?

'''
