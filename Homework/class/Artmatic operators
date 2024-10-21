import re

class PenezniHotovost:
    """
    Trida reprezentuje penezni hotovost v urcite mene
    """

    def __init__(self, castka: float, mena: str):
        """
        Pri vytvoreni tridy se musi specifikovat castka a mena, nebo se pouzije defaultnich 0 EUR

        :param castka: Jakekoli realne cislo, muze byt i zaporne
        :param mena: Mena vyjadrena jako tripismeny kod
        """
        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')

        self._mena = mena
        self._castka = castka

    def __str__(self):
        """
        Vrati castku a menu jako string
        :return: <castka> <mena>
        """
        return str(self._castka) + " " + self._mena

    def __add__(self, other):
        """
        Pretizeni operatoru + ktere vytvori novy objekt jako vysledek operace scitani
        :param other: Lze scitat cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace scitani
        """
        if isinstance(other, float) or isinstance(other, int):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other
            return vysledek

        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other._castka
            return vysledek

        raise Exception("Penezni hotovost lze scitat pouze s int, float a hotovosti ve stejne mene")

    def __sub__(self, other):
        """
        Pretizeni operatoru - ktere vytvori novy objekt jako vysledek operace odecteni
        :param other: Lze odečítat cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodních objektu a zustatek jako výsledek operace odcitani
        """
        if isinstance(other, float) or isinstance(other, int):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka - other
            return vysledek

        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka - other._castka
            return vysledek

        raise Exception("Penezni hotovost lze odcit pouze s int, float a hotovosti ve stejne mene")

    def __mul__(self, other):
        """
        Pretizeni operatoru * ktere vytvori novy objekt jako vysledek operace nasobeni
        :param other: Lze nasobit cissla typy int, float
        :return: Vrací novy objekt s nasobkem puvodni castky
        """
        if isinstance(other, float) or isinstance(other, int):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka * other
            return vysledek

        raise Exception("Penezni hotovost lze nasobit pouze s int nebo float")

    def __pow__(self, power, modulo=None):
        """
        Pretizeni operatoru ** ktere vytvori novy objekt jako vysledek umocneni
        :param power: mocnitel (int nebo float)
        :param modulo: volitelný argument pro modulo (není využito)
        :return: Vraci novy objekt s castkou umocněnou na power
        """
        if isinstance(power, (float, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka ** power
            return vysledek

        raise Exception("Mocnitel musi byt cislo typu int nebo float")

    def __iadd__(self, other):
        """
        Implementace operatori += ma za ukol secist hotovost a zachovat puvodni objekt
        :param other: Muze byt int, float nebo trida PenezniHotovost
        :return: Vraci stavajici objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace scitani
        """
        if (isinstance(other, float) or isinstance(other, int)):
            self._castka += other
            return self

        if (isinstance(other, PenezniHotovost) and other._mena == self._mena):
            self._castka += other._castka
            return self

        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")
    def __isub__(self, other):
        """
        Implementace operatori += ma za ukol odecist hotovost a zachovat puvodni objekt
        :param other: Muze byt int, float nebo trida PenezniHotovost
        :return: Vraci stavajici objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace odcitani
        """
        if (isinstance(other, float) or isinstance(other, int)):
            self._castka -= other
            return self

        if (isinstance(other, PenezniHotovost) and other._mena == self._mena):
            self._castka -= other._castka
            return self

        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")

    def __imul__(self, other):
        """
              Implementace operatori *= ma za ukol vynasobit hotovost a zachovat puvodni objekt
              :param other: Muze byt int, float nebo trida PenezniHotovost
              :return: Vraci stavajici objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace nasobeni
              """
        if (isinstance(other, float) or isinstance(other, int)):
            self._castka *= other
            return self

        if (isinstance(other, PenezniHotovost) and other._mena == self._mena):
            self._castka *= other._castka
            return self


vyplata = PenezniHotovost(1000, "CZK")
vyplata += 2000  # 1000 + 2000 = 3000
print(vyplata)
vyplata -= 500  # 3000 - 500 = 2500
print(vyplata)
