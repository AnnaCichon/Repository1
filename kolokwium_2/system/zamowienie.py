from system.developer import Developer


class Zamowienie:

    def __init__(self, domy: list, mieszkania: list, developer: Developer,
                 klient: str):
        self._domy = domy
        self._mieszkania = mieszkania
        self._developer = developer
        self._klient = klient

    def __str__(self):
        return f"Dane zamowienia: \n Domy: {self._domy} \n " \
               f"Mieszkania: {self._mieszkania} \n " \
               f"Developer: {self._developer} \n " \
               f"Klient: {self._klient} \n "

    def suma_powierchni(self):
        return round(sum(([mieszkanie._powierzchnia for mieszkanie
                           in self._mieszkania]
                          + [dom._powierzchnia for dom in self._domy])), 2)

    def wartosc_zamowienia(self):
        return round(sum(([mieszkanie._cena for mieszkanie
                           in self._mieszkania]
                          + [dom._cena for dom in self._domy])), 2)

    @property
    def domy(self) -> list:
        return self._domy

    @domy.setter
    def domy(self, value: list) -> None:
        self._domy = value

    @property
    def mieszkania(self) -> list:
        return self._mieszkania

    @mieszkania.setter
    def mieszkania(self, value: list) -> None:
        self._mieszkania = value

    @property
    def developer(self) -> Developer:
        return self._developer

    @developer.setter
    def developer(self, value: Developer) -> None:
        self._developer = value

    @property
    def klient(self) -> str:
        return self._klient

    @klient.setter
    def klient(self, value: str) -> None:
        self._klient = value


