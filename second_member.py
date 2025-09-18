# 5-цілочисельне ділення(//), 6-остача від ділення(%), 7-піднести в ступінь, 8-видобути корінь
def integer_division():
    print("  x // y = ?")
    number1 = int(input("Введіть x: "))
    number2 = int(input("Введіть y: "))
    if number2 == 0:
        print("   На жаль це буде нескінченність!")
    else:
        result = number1 // number2
        print(f"   {number1} // {number2} = {result}")
    # if b == 0:
    #     return "Помилка: ділення на нуль!"
    # return a // b


def remainder_of_dividing():
    print("  x % y = ?")
    number1 = int(input("Введіть x: "))
    number2 = int(input("Введіть y: "))
    if number2 == 0:
        print("   На жаль це буде нескінченність!")
    else:
        result = number1 % number2
        print(f"   {number1} % {number2} = {result}")
    # if b == 0:
    #     return "Помилка: ділення на нуль!"
    # return a % b


def power():
    print("  x ** y = ?")
    number1 = int(input("Введіть x: "))
    number2 = int(input("Введіть y: "))
    result = number1 ** number2
    print(f"   {number1} ** {number2} = {result}")
    # return a ** b


def root():
    print("  x ** 1/y = ?")
    number1 = int(input("Введіть x: "))
    number2 = int(input("Введіть y: "))
    if number1 < 0 and number2 % 2 == 0:
        print("   Помилка: не можна видобути парний корінь з від’ємного числа!")
    else:
        result = number1 ** (1 / number2)
        print(f"   {number1} ** (1/{number2}) = {result}")
    # return a ** (1 / n)
