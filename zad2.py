from zad1 import Student

class Library:

    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka: {self.city}, {self.street}, {self.zip_code}, {self.open_hours}, {self.phone} \n'

class Order:
    def __init__(self, Employee, Student, Books, order_date):
        self.employee = Employee
        self.student = Student
        self.books = Books
        self.order_date = order_date

    def __str__(self):
        return f'Zamówienie: {self.order_date} \n {self.employee} {self.student} \n {self.books}'

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Pracownik: {self.first_name}, {self.last_name}, {self.hire_date}, {self.birth_date}, {self.city}, {self.street}, {self.zip_code}, {self.phone} \n'


class Book:
    def __init__(self, Library, publication_date, author_name, author_surname, number_of_pages):
        self.library = Library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Ksiazka: {self.publication_date}, {self.author_name}, {self.author_surname}, {self.number_of_pages} \n z {self.library}'

if __name__=="__main__":

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