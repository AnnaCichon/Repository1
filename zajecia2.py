#a
def imiona(lista):
    for i in range(5):
        print(lista[i])

#print(imiona(['Tomasz', 'Anna', 'Piotr', 'Martyna', 'Adam']))


# a`
def imiona1(lista):
    return ','.join(lista)

#print(imiona1(['Tomasz', 'Anna', 'Piotr', 'Martyna', 'Adam']))

#b
def liczby(lista):
    x = []
    for i in lista:
        x.append(i*2)
    return x

# print(liczby([1, 2, 3, 4, 5]))

#b`
def liczby1(lista):
    x = [i*2 for i in lista]
    return x

# print(liczby1([1, 2, 3, 4, 5]))

#c
def parzyste(lista):
    for i in lista:
        if i % 2 == 0:
            print(i)

# print(parzyste([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

#c`
def parzyste1(lista):
    x = [i for i in lista if i % 2 == 0]
    return x

# print(parzyste1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

#d
def drugi_element(lista):
    x = [lista[i] for i in range(10) if i % 2 == 0]
    return x

print(drugi_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
