from klasy.firma import Firma


class FirmaTransportowa(Firma):

    def __init__(self, nazwa: str, wlasciciel: str, nip: str,
                 miasto: str, kod_pocztowy: str, ulica: str,
                 telefon: int, dzialalnosc: str, rodzaj_transportu: str):
        super().__init__(nazwa, wlasciciel, nip,
                         miasto, kod_pocztowy, ulica,
                         telefon, dzialalnosc)
        self._rodzaj_transportu = rodzaj_transportu

    def __str__(self):
        return f"Dane firmy transportowej: \n Nazwa: {self._nazwa} \n " \
               f"Wlasciciel: {self._wlasciciel} \n " \
               f"Nip: {self._nip} \n Adres: {self._ulica} " \
               f"{self._kod_pocztowy} {self._miasto} \n " \
               f"Telefon: {self._telefon} \n " \
               f"Dzialalnosc: {self._dzialalnosc} \n " \
               f"Rodzaj transportu: {self._rodzaj_transportu} \n"

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

    @property
    def rodzaj_transporu(self) -> str:
        return self._rodzaj_transportu
