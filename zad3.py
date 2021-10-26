class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Posiadlosc: {self.area} m^3, {self.rooms}, {self.price} zl, {self.address}'

class House(Property):

    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Dom: {self.area} m^3, {self.rooms}, {self.price} zl, {self.address}, {self.plot} m^2'

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Mieszkanie: {self.area}, m^3, {self.rooms}, {self.price} zl, {self.address}, {self.floor}'


if __name__=="__main__":

    posiadlosc = Property(90, 3, 500000, 'Wisniowa 5')

    dom = House(120, 6, 1000000, 'Wisniowa 5', 1000)
    print(dom)
    mieszkanie = Flat(60, 2, 450000, 'Grunwaldzka 3', 4)
    print(mieszkanie)