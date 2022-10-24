# Напишите набор из шести операторов class для моделирования такой иерархической
# классификации с помощью наследования Python. Затем добавьте в каждый класс
# метод speak, выводящий уникальное сообщение, а в суперкласс верхнего уровня
# Animal — метод reply, который просто вызывает self. speak, чтобы запустить
# инструмент вывода, специфичный для категории, из подкласса ниже в дереве
# (это инициирует независимый поиск при наследовании из self). Наконец, удалите
# метод speak из класса Hacker, чтобы он выбирал стандартный метод, находящийся
# выше. Когда вы завершите, ваши классы должны работать следующим образом:

class Animal:
    def speak(self):
        pass

    def reply(self):
        self.speak()


class Mammal(Animal):
    def speak(self):
        print('ррр')


class Cat(Mammal):
    def speak(self):
        print('мяу')


class Dog(Mammal):
    def speak(self):
        print('гав')


class Primate(Mammal):
    def speak(self):
        print('Hello world!')


class Hacker(Primate):
    pass


spot = Cat()
spot.reply()  # Animal.reply: вызывает Cat.speak

data = Hacker()  # Animal.reply: вызывает Primate.speak
data.reply()
