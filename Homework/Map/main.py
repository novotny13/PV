

Stredocesky = ["Dobřichovice","Dobříš"]
Ustecky = ["Ústí nad Labem","Děčín"]
Liberecky = ["Liberec"]
regions = {
    "Ustecky": Ustecky,
    "Liberecky": Liberecky,
    "Stredocesky": Stredocesky,
}
input = input("Enter the name of desired City Or")
if input in regions:
    print(regions[input])
elif input in Liberecky:
    print("Liberecky kraj")
elif input in Ustecky:
    print("Ustecky kraj")
elif input in Stredocesky:
    print("Stredocesky kraj")