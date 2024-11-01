
Labe = {
    "pramen": " in Krkonose",
    "nazev": "Labe",
    "flows through":  ["Usti", "Roudnice", "Melnik"]
}
Berounka = {
    "pramen": " in Plzen",
    "nazev": "Berounka",
    "flows through":  ["Mokropsy", "Zadní Třebáň", "Nižbor"]
}
Luznice = {
    "pramen": " on Kralicky Sneznik",
    "nazev": "Luznice",
    "flows through":  ["Frahelž", "Bechyně", "Stará Hlína"]
}
rivers = { "Labe" :Labe,"Berounka" : Berounka,"Luznice" : Luznice}
input = input("Enter the name of an River or an City: ")
if input in rivers:
    print("source is {} and it flows through {}".format(rivers[input]["pramen"],rivers[input]["flows through"]))
if input in Labe["flows through"]:
    print("Labe")
if input in Berounka["flows through"]:
    print("Berounka")
if input in Luznice["flows through"]:
    print("Luznice")