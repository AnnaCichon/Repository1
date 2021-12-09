from klasy.pojazd import Pojazd
from klasy.firma_transportowa import FirmaTransportowa
from klasy.firma_spozywcza import FirmaSpozywcza


class Kurs:

    def __init__(self, pojazd: Pojazd, kierowca: str, odcinki: list,
                 firma_transportowa: FirmaTransportowa,
                 firma_spozywcza: FirmaSpozywcza):
        self._pojazd = pojazd
        self._kierowca = kierowca
        self._odcinki = odcinki
        self._firma_transportowa = firma_transportowa
        self._firma_spozywcza = firma_spozywcza

    def __str__(self):
        return f"Dane na temat kursu: \n Pojazd: {self._pojazd} \n " \
               f"Kierowca: {self._kierowca} \n " \
               f"Odcinki: {self._odcinki} \n " \
               f"Firma transportowa: {self._firma_transportowa} \n " \
               f"Firma Spozywca: {self._firma_spozywcza} \n"

    def marka_pojazdu(self):
        return self._pojazd._marka

    def suma(self):
        return round(sum([odcinek._odleglosc for odcinek in self._odcinki]), 2)

    @property
    def pojazd(self) -> Pojazd:
        return self._pojazd

    @pojazd.setter
    def pojazd(self, value: Pojazd) -> None:
        self._pojazd = value

    @property
    def kierowca(self) -> str:
        return self._kierowca

    @kierowca.setter
    def kierowca(self, value: str) -> None:
        self._kierowca = value

    @property
    def odcinki(self) -> list:
        return self._odcinki

    @odcinki.setter
    def odcinki(self, value: list) -> None:
        self._odcinki = value

    @property
    def firma_transportowa(self) -> FirmaTransportowa:
        return self._firma_transportowa

    @firma_transportowa.setter
    def firma_transportowa(self, value: FirmaTransportowa) -> None:
        self._firma_transportowa = value

    @property
    def firma_spozywcza(self) -> FirmaSpozywcza:
        return self._firma_spozywcza

    @firma_spozywcza.setter
    def firma_spozywcza(self, value: FirmaSpozywcza) -> None:
        self._firma_spozywcza = value
