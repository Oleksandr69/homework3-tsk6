# 5-цілочисельне ділення(//), 6-остача від ділення(%), 7-піднести в ступінь, 8-видобути корінь
def integer_division(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a // b


def remainder_of_dividing(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a % b


def power(a, b):
    return a ** b


def root(a, n=2):
    if a < 0 and n % 2 == 0:
        return "Помилка: не можна видобути парний корінь з від’ємного числа!"
    return a ** (1 / n)
