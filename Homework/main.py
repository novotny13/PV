Labe = {
    "Name": "Labe",
    "Source": " in Krkonose",
    "flowsinto": " Sea",
    "endPlace": "Hamburg"
}
Vltava = {
    "Name": "Vltava",
    "Source": " in Sumava",
    "flowsinto": "Labe",
    "endPlace": "Melnik"
}
Berounka = {
    "Name": "Berounka",
    "Source": " Lysá",
    "flowsinto": " Vltava",
    "endPlace": "Praha"
}
Mze = {
    "Name": "Mze",
    "Source": " Griesbacher Wald",
    "flowsinto": " Berounka",
    "endPlace": "Plzen"

}
Radbuza = {
    "Name": "Radbuza",
    "Source": " in Krkonose",
    "flowsinto": " Berounka",
    "endPlace": "Plzen"

}
Strela = {
    "Name": "Strela",
    "Source": " in Prachomety",
    "flowsinto": " Berounka",
    "endPlace": "Libin"
}
rivers = { "Labe" :Labe,"Vltava" :Vltava,"Berounka" :Berounka,"Mze" :Mze,"Strela" :Strela,"Radbuza" :Radbuza}
input = input("Enter the name of an River: ")
if input in rivers:
    print(rivers[input])
print("Th rivers that flow into {}".format(rivers[input]["Name"]))
for x in rivers:
    x = rivers[x]
    if rivers[input]["Name"] in x["flowsinto"]:
     print(x["Name"])


