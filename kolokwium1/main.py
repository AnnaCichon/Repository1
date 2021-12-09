from klasy.odcinek import Odcinek
from klasy.firma_spozywcza import FirmaSpozywcza
from klasy.kurs import Kurs
from klasy.pojazd import Pojazd
from klasy.firma_transportowa import FirmaTransportowa

if __name__ == "__main__":

    firma_spozywcza1 = FirmaSpozywcza('ABC', 'Jan Kowalski', '123-456-32-18',
                                      'Wroclaw', '42-612', 'Wloska 5',
                                      621458789, 'spozywcza', 'warzywniak')

    firma_transportowa1 = FirmaTransportowa('Nowak', 'Anna Nowak',
                                            '321-256-32-18', 'Poznan',
                                            '42-606', 'Pastuszki 6', 694258735,
                                            'transportowa',
                                            'drogowo- samochodowy')

    pojazd1 = Pojazd('Peugeot Boxer', 150, 1500, 'STA1612C', 192)

    odcinek1 = Odcinek('Punkt A', 'Punkt B', 250, '4:00', 1)
    odcinek2 = Odcinek('Punkt C', 'Punkt D', 350, '5:30', 2)
    odcinek3 = Odcinek('Punkt E', 'Punkt F', 134, '1:20', 3)

    kurs1 = Kurs(pojazd1, 'Tomasz Pal', [odcinek1, odcinek2, odcinek3],
                 firma_transportowa1, firma_spozywcza1)

    print(kurs1)
    print(kurs1.marka_pojazdu())
    print(kurs1.suma())
