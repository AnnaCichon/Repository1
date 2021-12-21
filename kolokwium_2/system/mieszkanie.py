from system.nieruchomosc import Nieruchomosc


class Mieszkanie(Nieruchomosc):

    def __init__(self, powierzchnia: float, pokoje: int, cena: int,
                 miasto: str, kod_pocztowy: str, ulica: str,
                 rodzaj_nieruchomosci: str, pietro: int):
        super().__init__(powierzchnia, pokoje, cena,
                 miasto, kod_pocztowy, ulica, rodzaj_nieruchomosci)
        self._pietro = pietro

    def __str__(self):
        return f"Opis mieszkania: \n Powierzchnia: {self._powierzchnia} \n " \
               f"Ilosc pokoi: {self._pokoje} \n " \
               f"Cena: {self._cena} \n " \
               f"Adres: {self._ulica} {self._kod_pocztowy} " \
               f"{self._miasto} \n " \
               f"Rodzaj nieruchomosci: {self._rodzaj_nieruchomosci} \n" \
               f"Piętro: {self._pietro} \n"

    @property
    def powierzchnia(self) -> float:
        return self._powierzchnia

    @property
    def pokoje(self) -> int:
        return self._pokoje

    @property
    def cena(self) -> int:
        return self._cena

    @property
    def miasto(self) -> str:
        return self._miasto

    @property
    def kod_pocztowy(self) -> str:
        return self._kod_pocztowy

    @property
    def ulica(self) -> str:
        return self._ulica

    @property
    def rodzaj_nieruchomosci(self) -> str:
        return self._rodzaj_nieruchomosci

    @property
    def pietro(self) -> int:
        return self._pietro

