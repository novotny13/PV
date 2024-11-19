def vydej_obedu():
    menu = [
         "vitamínový nápoj",
         "polévka česneková s bramborem",
         "segedínský guláš, houskové knedlíky",
         "jablko",
    ]
    yield  menu[0]

    vyber = yield "Vyber si A nebo B menu"
    print(vyber)
    if vyber == "A":
        jidlo = str(menu[1])
    if vyber == "B":
        jidlo = str(menu[2])
    yield jidlo



k = vydej_obedu()

piti = next(k)
print(piti)

odpoved = next(k)
print(odpoved)

odpoved = k.send("B")
print(odpoved)

k.close()