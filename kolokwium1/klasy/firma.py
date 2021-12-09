class Firma:

    def __init__(self, nazwa: str, wlasciciel: str, nip: str,
                 miasto: str, kod_pocztowy: str, ulica: str,
                 telefon: int, dzialalnosc: str) -> None:

        self._nazwa = nazwa
        self._wlasciciel = wlasciciel
        self._nip = nip
        self._miasto = miasto
        self._kod_pocztowy = kod_pocztowy
        self._ulica = ulica
        self._telefon = telefon
        self._dzialalnosc = dzialalnosc

    def __str__(self):
        return f"Dane firmy: \n Nazwa: {self._nazwa} \n " \
               f"Wlasciciel: {self._wlasciciel} \n " \
               f"Nip: {self._nip} \n " \
               f"Adres: {self._ulica} {self._kod_pocztowy} " \
               f"{self._miasto} \n " \
               f"Telefon: {self._telefon} \n " \
               f"Dzialalnosc: {self._dzialalnosc} \n "

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def wlasciciel(self) -> str:
        return self._wlasciciel

    @property
    def nip(self) -> str:
        return self._nip

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
    def telefon(self) -> int:
        return self._telefon

    @property
    def dzialalnosc(self) -> str:
        return self._dzialalnosc
