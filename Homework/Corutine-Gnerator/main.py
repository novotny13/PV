def generatorITVelikanu():
    yield "Alan Turing"
    yield "Steave Jobs"
    yield "John von Neumann"

print("Velikani v IT")
for osoba in generatorITVelikanu():
    print(osoba)