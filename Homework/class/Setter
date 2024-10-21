class Obdelnik:
    def __init__(self):
        self._StranaA = 0
        self._StranaB = 0

    @property
    def StranaA(self):
        return self._StranaA

    @StranaA.setter
    def StranaA(self,a):
        if(a  < 0):
            raise Exception("Zaporna vaha nesmi existovat")

        self._StranaA = a

    @property
    def StranaB(self):
        return self._StranaB

    @StranaB.setter
    def StranaB(self, b):
        if (b < 0):
            raise Exception("Zaporna vaha nesmi existovat")

        self._StranaB = b
    def __str__(self):
        return f"A: {self._StranaA} B: {self._StranaB}"

ob = Obdelnik()
ob.StranaA = 10
ob.StranaB = 20
print(ob)
