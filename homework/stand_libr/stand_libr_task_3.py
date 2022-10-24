# Напишите игру Кости

from random import randint


MIN_DICE_VALUE = 1
MAX_DICE_VALUE = 6


def throw_dice():
    return randint(MIN_DICE_VALUE, MAX_DICE_VALUE)


if __name__ == '__main__':
    dice_1 = throw_dice()
    dice_2 = throw_dice()

    print('Ваш результат:', dice_1, dice_2)
