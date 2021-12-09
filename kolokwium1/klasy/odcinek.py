from klasy.kurs import Kurs


class Odcinek:
    def __init__(self, start: str, koniec: str, odleglosc: float,
                 czas_przejazdu: str, numer_odcinka: int):
        self._start = start
        self._koniec = koniec
        self._odleglosc = odleglosc
        self._czas_przejazdu = czas_przejazdu
        self._numer_odcinka = numer_odcinka

    def __str__(self):
        return f"Dane na temat odcinka kursu: \n Start: {self._start} \n " \
               f"Koniec: {self._koniec} \n " \
               f"Odleglosc: {self._odleglosc} km \n " \
               f"Czas przejazdu: {self._czas_przejazdu} h \n " \
               f"Numer odcinka: {self._numer_odcinka} \n"

    @property
    def start(self) -> str:
        return self._start

    @property
    def koniec(self) -> str:
        return self._koniec

    @property
    def odleglosc(self) -> float:
        return self._odleglosc

    @property
    def czas_przejazdu(self) -> str:
        return self._czas_przejazdu

    @property
    def numer_odcinka(self) -> int:
        return self._numer_odcinka
