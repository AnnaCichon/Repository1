class Zlecenie:
    def __init__(self, id_zlecenia: int) -> None:
        self._id_zlecenia = id_zlecenia

    def __str__(self):
        return f'{self._id_zlecenia}'



class FirmaSpozywcza(Zlecenie):

    def __init__(self, nazwa_firmy: str, imie_wlasciciela: str, nazwisko_wlasciciela: str, adres_firmy: str, telefon: int, id_zlecenia: int) -> None:
        super().__init__(id_zlecenia)
        self._nazwa_firmy = nazwa_firmy
        self._imie_wlasciciela = imie_wlasciciela
        self._nazwisko_wlasciciela = nazwisko_wlasciciela
        self._adres_firmy = adres_firmy
        self._telefon = telefon

    def __str__(self):
        return f'{self._id_zlecenia}, {self._nazwa_firmy}'

class FirmaTransportowa(Zlecenie):

    def __init__(self, nazwa: str, imie: str, nazwisko: str, adres: str, telefon: int, id_zlecenia: int) -> None:
        super().__init__(id_zlecenia)
        self._nazwa = nazwa
        self._imie = imie
        self._nazwisko= nazwisko
        self._adres = adres
        self._telefon = telefon

    def __str__(self):
        return f'{self._nazwa}, {self._adres}'

class Pojazd(Zlecenie):

    def __init__(self, marka: str, numer_pojazdu: int, pojemnosc: int, kierowca: str, id_zlecenia: int) -> None:
        super().__init__(id_zlecenia)
        self._marka = marka
        self._numer_pojazdu = numer_pojazdu
        self._pojemnosc = pojemnosc
        self._kierowca = kierowca

    def __str__(self):
        return f'{self._numer_pojazdu}'


class Odcinek(Zlecenie):

    def __init__(self, skad: int, dokad: int, numer_odcinka: int, kierowca: str, odleglosc: int, id_zlecenia: int, Kurs) -> None:
        super().__init__(id_zlecenia)
        self._skad = skad
        self._dokad = dokad
        self._numer_odcinka = numer_odcinka
        self.kierowca = kierowca
        self._odleglosc = odleglosc
        self._kurs = Kurs

class Kurs(Zlecenie):

    def __init__(self, id_zlecenia, odcinki: lst, odleglosci_odcinkow, Pojazd, marka, numer_kursu: int):
        super().__init__(id_zlecenia)
        self._odcinki = odcinki
        self._odleglosci_odcinkow = odleglosci_odcinkow
        self._pojazd = Pojazd
        self._marka = marka
        self._numer_kursu= numer_kursu

    @ property
    def odcinki(self):
            return sum(odcinki)

    def __str__(self):
        return f'{self._numer_kursu}'


if __name__=="__main__":

    kurs1 = Kurs()
    print(kurs1)


