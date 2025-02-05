# Создание классов

# class <имя класса>:
#    <описание класса>

# Свойства объектов называются атрибутами

# Для создания или изменения значения атрибута используется следующий синтаксис:

# <имя объекта > . < имя атрибута > = < значение >
# Действия объектов называются методами

# def <имя метода>(self, <аргументы>):
#    <тело метода>
# Для создания объектов класса,нужно использовать следующий синтаксис:
# <имя оъекта> = <имя класса>(<аргументы метода _innit_()>)


class Car:

    def _init_(self, color, consumption, tank_volume, mileage=0):
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.maleage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен"
        return "Двигатель уже был запущен"

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен"
        return "Двигатель уже был остановлен"

    def drave(self, distance):
        if not self.engien_on:
            return 'Двигатель не запущен'
        if self.reserve / self.consumption * 100 < distance:
            return 'Малый запас топлива'
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток топлива {self.reserve} л."

    def refuel(self):
        self.reserve = self.tank_volume

    def get_mileage(self):
        return self.mileage

    def get_resreve(self):
        return self.reserve


car_1 = Car(color='black', consumptoin=10, tank_volume=55)

print(car_1.start_engine())
print(car_1.drave(100))
print(car_1.drave(100))
print(car_1.drave(100))
print(car_1.drave(300))
print(f"Пробег {car_1.get_mileage()} км.")
print(f"Запас топлива {car_1.get_reserve()} л.")
print(car_1.stop_engine())
print(car_1.drave(100))
