import math


while True:
    try:

        radius = int(input("Zadej cislo: "))
        if radius <= 0:
            raise ArithmeticError("No")

    except ArithmeticError:
        print("Try again")
    except ValueError:
        print("Try again")
    else:
        break
result = math.pi * (radius ** 2)
print(result)