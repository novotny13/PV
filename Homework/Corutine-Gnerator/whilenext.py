
def generatorKrasovychJezerCR():
    try:
        yield "Horní macošské jezírko"
        yield "Chalupská slať"
        yield "Rejvíz"
        yield "PP Jezírko pod Táborem"
        yield "jezírko v Hranické propasti"
        yield "	Úpské rašeliniště"
        yield "PP Rašelinné jezírko Rosička"

    except GeneratorExit:
        print("!Generovani preruseno!")




print("Raselinova jezera v CR")

mesta = generatorKrasovychJezerCR()

while True:

    try:
        print(next(mesta))

    except StopIteration:
        break

