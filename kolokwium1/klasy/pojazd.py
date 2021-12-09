class Pojazd:

    def __init__(self, marka: str, przebieg: int, pojemnosc: int,
                 rejestracja: str, moc: int):
        self._marka = marka
        self._przebieg = przebieg
        self._pojemnosc = pojemnosc
        self._rejestracja = rejestracja
        self._moc = moc

    def __str__(self):
        return f"Dane pojazdu: \n Marka: {self._marka} \n " \
               f"Przebieg: {self._przebieg} tys km \n " \
               f"Pojemnosc: {self._pojemnosc} kg \n " \
               f"Rejestracja: {self._rejestracja} \n " \
               f"Moc: {self._moc} \n"

    @property
    def marka(self) -> str:
        return self._marka

    @property
    def przebieg(self) -> int:
        return self._przebieg

    @property
    def pojemnosc(self) -> int:
        return self._pojemnosc

    @property
    def rejestracja(self) -> str:
        return self._rejestracja

    @property
    def moc(self) -> int:
        return self._moc
