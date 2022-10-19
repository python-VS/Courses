# Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите
# методы addition — сложение, multiplication — умножение, division — деление,
# subtraction — вычитание. При вызове методов с параметрами a и b нужно
# производить соответствующие действия и печатать ответ.


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


math = Math(10, 3)
print(f'addition result {math.addition()}')
print(f'multiplication result {math.multiplication()}')
print(f'division result {math.division()}')
print(f'subtraction result {math.subtraction()}')
