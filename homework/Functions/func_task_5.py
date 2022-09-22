# Написать функцию-декоратор, которая вычисляет время выполнения декорируемой функции,
# а также выводит на экран имя функции и ее параметры.

def my_dec(func):
    def wrapper(*args, **kwargs):
        # operations_before_run
        result = func(*args, **kwargs)
        # operations_after_run
        return result
    return wrapper

#Декорирование функции происходит посредством следующего синтаксиса

@decorator
def func():
    pass
