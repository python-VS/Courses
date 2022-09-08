# Создайте дочерний класс Bus, который наследуется от класса Vehicle.
# Плата за проезд (fare) по умолчанию для любого транспортного
# средства составляет вместимость (capacity) * 100.
# Если транспортное средство является экземпляром автобуса,
# нам нужно добавить дополнительные 10% к полной стоимости проезда
# в качестве платы за обслуживание.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return super().fare() * 1.1

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())