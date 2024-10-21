Třída Auto má následující atributy:
1.
objem_nadrze_l: Maximální kapacita nádrže v litrech.
spotreba_na_100_km_l: Spotřeba paliva v litrech na 100 km.
_aktualni_objem_paliva_v_nadrzi_l: Aktuální množství paliva v nádrži (private atribut).

2.
Public atributy (jsou přístupné zvenčí):
objem_nadrze_l
spotreba_na_100_km_l

Private atributy (nejsou přístupné zvenčí, označené podtržítkem _):
_aktualni_objem_paliva_v_nadrzi_l

3.
Jak je řešen ve třídě princip zapouzdření, jak se manipuluje s private atributy?
Princip zapouzdření je řešen tak, že atribut _aktualni_objem_paliva_v_nadrzi_l je označen jako private (s podtržítkem) a není přímo přístupný zvenčí třídy. Manipulace s tímto atributem je možná pouze prostřednictvím metod:

natankuj(): Slouží k přidání paliva do nádrže.
popojed(): Odebírá palivo při jízdě.
aktualni_stav_nadrze(): Vrací aktuální stav paliva v nádrži.



class Auto:
    """ Trida auto reprezentuje auto pro simulaci realneho vozidlo pro cviceni PV na SPSE Jecna """

    def __init__(self, objem_nadrze_l : float, spotreba_na_100_km_l : float):
        """
        Konstruktor nastavi objem nadrze a spotrebu dle parametru a nastavi prazdnou nadrz.

        :param objem_nadrze_l: Objem nadrze v litrech
        :param spotreba_na_100_km_l: Spotreba na 100km v litrech
        """

        if (objem_nadrze_l < 0):
            raise Exception("Nadrz musi mit kladny objem")
        if (spotreba_na_100_km_l < 0):
            raise Exception("Spotreba nesmi byt zaporna")

        self.objem_nadrze_l = objem_nadrze_l
        self.spotreba_na_100_km_l = spotreba_na_100_km_l
        self._aktualni_objem_paliva_v_nadrzi_l = 0

    def aktualni_stav_nadrze(self) -> float:
        """
        Metoda vrati aktualni stav nadrze

        :return: Zbyle palivo v nadrzi v litrech
        """
        return self._aktualni_objem_paliva_v_nadrzi_l

    def natankuj(self, objem_l : float ) -> None:
        """
                 Metoda prida k aktualnimu stavu nadrze objem v litrech.
                 :objem_l: Pocet litru ktere metoda prida ke zbylemu palivu

        """

        if(objem_l < 0):
            raise Exception("Nelze odcerpat palivo pomoci metody natankovat")

        if((self._aktualni_objem_paliva_v_nadrzi_l + objem_l) > self.objem_nadrze_l):
            raise Exception("Nelze nacerpat vice nez je kapacita nadrze")

        self._aktualni_objem_paliva_v_nadrzi_l += objem_l

    def popojed(self, pocet_km : float ) -> None:

        """
            Metoda odebere pocet litru z nadrze podle poctu kilometru a podle spotreby auta.
            :pocet_km: Vzdalenost kterou auto ujede v kilometrech
        """
        if(pocet_km < 0):
            raise Exception("Couvani je take jizda, smer neresime")

        spotreba_paliva_l = pocet_km/100.0 * self.spotreba_na_100_km_l

        if(self._aktualni_objem_paliva_v_nadrzi_l < spotreba_paliva_l):
            raise Exception("Na jizdu neni dostatek paliva")

        self._aktualni_objem_paliva_v_nadrzi_l -= spotreba_paliva_l


#my code-----------------------------------------------------

auto = Auto(objem_nadrze_l=30.0, spotreba_na_100_km_l=12.5)

auto.natankuj(22.5)

auto.popojed(20)
