



while True:
    try:
        while len(x)>100:
            x = int(input("Zadej cislo: "))

    except ValueError:
        print("Try again")
    else:
        break
y = int(x) + 1
print(y)