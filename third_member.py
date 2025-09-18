import math
# 9-sin(x), 10-cos(x), 11-tng(x), 12-чи парне x
def sin():
    print("  sin(x) = ?")
    number = int(input("Введіть x: "))
    result = math.sin(number)
    print(f"   sin({number}) = {result}")

def cos():
    print("  cos(x) = ?")
    number = int(input("Введіть x: "))
    result = math.cos(number)
    print(f"   cos({number}) = {result}")

def tg():
    print("  tg(x) = ?")
    number = int(input("Введіть x: "))
    result = math.tan(number)
    print(f"   tg({number}) = {result}")

def is_even():
    print("is x even ?")
    number = int(input("Введіть x: "))
    if number % 2 == 0:
        print(f"   {number} is even.")
    else:
        print(f"   {number} is not even.")
