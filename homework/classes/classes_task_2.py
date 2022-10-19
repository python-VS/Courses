# Напишите программу с классом Car. Создайте инициализатор класса Car.
# Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится
# сообщение «Автомобиль заведен». Второй — отключение автомобиля — выводит
# сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года
# выпуска. Четвертый метод — присвоение автомобилю типа. Пятый —
# присвоение автомобилю цвета.


class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    @staticmethod
    def start():
        print("Автомобиль заведен")

    @staticmethod
    def stop():
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return f'{self.color} {self.type} {self.year}'


car = Car('серый', 'пежо', 2016)
print(car)
print(car.start())
print(car.stop())

car.set_year(2015)
print(car)

car.set_type('бмв')
print(car)

car.set_color('черный')
print(car)