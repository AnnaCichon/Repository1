class Developer:

    def __init__(self, imie: str, nazwisko: str, telefon: int,
                 ilosc_nieruchomosci: int):
        self._imie = imie
        self._nazwisko = nazwisko
        self._telefon = telefon
        self._ilosc_nieruchomosci = ilosc_nieruchomosci

    def __str__(self):
        return f"Dane developera: \n Imie: {self._imie} \n " \
               f"Nazwisko: {self._nazwisko} \n " \
               f"Telefon: {self._telefon} \n " \
               f"Ilosc nieruchomosci: {self._ilosc_nieruchomosci} \n "

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def telefon(self) -> int:
        return self._telefon

    @property
    def ilosc_nieruchomosci(self) -> int:
        return self._ilosc_nieruchomosci

