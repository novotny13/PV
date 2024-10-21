
class NoDeclaration(Exception):
    "Raised always"
    pass
class KonfiguraceKonference:

    _maximalni_pocet_ucastniku = 0
    def __new__(cls, *args, **kwargs):
        raise NoDeclaration




    @classmethod
    def set_maximalni_pocet_ucastniku(cls, max):
        cls._maximalni_pocet_ucastniku = max;

    @classmethod
    def get_maximalni_pocet_ucastniku(cls):
        return cls._maximalni_pocet_ucastniku;

try:
    print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())

    KonfiguraceKonference.set_maximalni_pocet_ucastniku(212)
    print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())


    mojeKonfigurace = KonfiguraceKonference()
    mojeKonfigurace.set_maximalni_pocet_ucastniku(300)
    print(mojeKonfigurace.get_maximalni_pocet_ucastniku())
except NoDeclaration:
    
        print("NO")
