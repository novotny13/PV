# Přepodkládejte následující kolekci:

zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "category" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "category" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "category" : (4, "Sluchátka")
    }
]
# Pomocí funkce sorted(zbozi, .... ) seřaďte zboží:
# podle ceny vzestupně
# podle názvu sestupně
# podle pořadí kategorie vzestupně

sorted_resault = lambda *x: sorted(*x, key=lambda x: (x["price"],x["category"]) )
sorted_category = lambda *x: sorted(*x, key=lambda x: x["category"] )
sorted_name = lambda *x: sorted(*x, key=lambda x: x["name"] )
print(sorted_resault(zbozi))
print(sorted_category(zbozi))
print(sorted_name(zbozi))