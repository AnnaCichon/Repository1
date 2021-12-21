from system.developer import Developer
from system.dom import Dom
from system.mieszkanie import Mieszkanie
from system.zamowienie import Zamowienie


if __name__ == "__main__":

    mieszkanie1 = Mieszkanie(60, 2, 300000, "Wroclaw", "42-512",
                             "Pastuszki 8", "mieszkanie", 3)
    mieszkanie2 = Mieszkanie(90, 3, 500000, "Katowice", "42-606",
                             "Wloska 124", "mieszkanie", 4)


    dom1 = Dom(200, 6, 1000000, "Warszawa", "42-512",
               "Włoska 7", "dom", 300)

    developer1 = Developer("Anna", "Nowak", 694123859, 3)

    zamowienie1 = Zamowienie([dom1], [mieszkanie1, mieszkanie2],
                             developer1, "Jan Kowalski")

    print(zamowienie1)

