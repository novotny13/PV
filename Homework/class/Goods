class Zbozi:
    def __new__(cls, nazev, cena):
        if nazev is None or not isinstance(cena, (int, float)) or cena < 0:
            instance = None
        else:
            instance = super().__new__(cls)

        return instance

    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena
    def __str__(self):
        return f"Nazev: {self.nazev}, cena: {self.cena}"


a = Zbozi("Rohlik", 5)
b = Zbozi("Hackers item", -10)

print(a)
print(b)
