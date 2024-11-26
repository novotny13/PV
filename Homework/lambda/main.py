def scitani(a, b):
    if (isinstance(a,str) and not isinstance(b,str) or isinstance(b,str) and not isinstance(a,str)):
        raise ValueError('a and b must be of same type')
    if (type(a) not in (int, float, complex)or type(b) not in (int, float, complex)):
        raise TypeError('a and b must be integers or floats')

    return a + b

import unittest



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

class TestScitani(unittest.TestCase):


    def test_integer(self):
        self.assertEqual(scitani(1, 1),2)
        self.assertEqual(scitani(-1, 1), 0)
        self.assertEqual(scitani(1, -1), 0)
        self.assertEqual(scitani(2, 3), 5)

    def test_real(self):
        self.assertEqual(scitani(-2.5, +0.5), -2)
        self.assertEqual(scitani(+2.5, +0.1), 2.6)
        self.assertNotEquals(scitani(-2.511111, +0.0), -2)
        self.assertNotEquals(scitani(-2.5, +0.0), -2)
    def test_complex(self):
        self.assertEqual(scitani(3, + 4j), 3+4j)
        self.assertNotEqual(scitani(+2.5j, -0.1), 2.4j)
        self.assertEquals(scitani(-2.511111, +0.0j), -2.511111)


    def test_bad_input(self):
        auto = Auto(objem_nadrze_l=30.0, spotreba_na_100_km_l=12.5)
        with self.assertRaises(ValueError):
            scitani("AHOJ", 100)
        with self.assertRaises(ValueError):
            scitani(100, "AHOJ")
        with self.assertRaises(TypeError):
            scitani(None, None)
        with self.assertRaises(TypeError):
            scitani([4, 5, 6], [1, 2, 3])
        with self.assertRaises(TypeError):
            scitani([4, 5, 6], True)
        with self.assertRaises(TypeError):
            scitani([4, 5, 6], auto)
        with self.assertRaises(ValueError):
            scitani("❤❤❤", True)
        with self.assertRaises(TypeError):
            scitani("❤❤❤", True)


if __name__ == '__main__':
    unittest.main()