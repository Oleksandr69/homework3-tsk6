def add():
    print("  x + y = ?")
    number1 = int(input("Введіть x: "))
    number2 = int(input("Введіть y: "))
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")

def subtraction():
    print("  x - y = ?")
    number1 = int(input("Введіть x: "))
    number2 = int(input("Введіть y: "))
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")

def multiplication():
    print("  x * y = ?")
    number1 = int(input("Введіть x: "))
    number2 = int(input("Введіть y: "))
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")

def division():
    print("  x / y = ?")
    number1 = int(input("Введіть x: "))
    number2 = int(input("Введіть y: "))
    if number2 == 0:
        print("На жаль це буде нескінченність!")
    else:
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")

