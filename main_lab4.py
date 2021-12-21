from zad2 import *
from zad3 import *

student1 = Student('Tomasz', 65)
student2 = Student('Aleksandra', 50)
print(student1.is_passed())
print(student2.is_passed())

biblioteka1 = Library('Warszawa', 'Wloska 12', '42-608', '10:00 - 16:00', 654123987)
biblioteka2 = Library('Katowice', 'Dworcowa 3', '68-238', '08:00 - 14:00', 654123258)

ksiazka1 = Book(biblioteka1, '16-10-2002', 'Stephen', 'King', 500)
ksiazka2 = Book(biblioteka2, '15-10-2001', 'J.K', 'Rowling', 400)
ksiazka3 = Book(biblioteka1, '15-12-1997', 'Agatha', 'Christie', 334)
ksiazka4 = Book(biblioteka2, '22-04-1998', 'Nicholas', 'Sparks', 506)
ksiazka5 = Book(biblioteka1, '06-10-1996', 'J.R.R', 'Tolkien', 679)

pracownik1 = Employee('Mariola', 'Waloszczyk', '25-10-2021', '12-01-2000', 'Warszawa', 'Pastuszki 7', '42-505', 543698787)
pracownik2 = Employee('Adam', 'Kowalski', '23-10-1998', '01-01-1978', 'Katowice', 'Dworcowa 7', '42-882', 693258744)
pracownik3 = Employee('Anna', 'Kula', '25-08-1989', '12-03-1966', 'Katowice', 'Wiejska 56', '36-555', 639258454)

student1 = Student('Tomasz', 65)
student2 = Student('Aleksandra', 50)
student3 = Student('Marta', 90)

zamowienie1 = Order(pracownik1, student1, ksiazka4, '26-10-2021')
zamowienie2 = Order(pracownik3, student2, ksiazka5, '22-06-2018')

print(zamowienie1)
print(zamowienie2)

posiadlosc = Property(90, 3, 500000, 'Wisniowa 5')

dom = House(120, 6, 1000000, 'Wisniowa 5', 1000)
print(dom)
mieszkanie = Flat(60, 2, 450000, 'Grunwaldzka 3', 4)
print(mieszkanie)