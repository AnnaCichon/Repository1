# ZAD 1


def typ_tekstowy(name: str, surname: str) -> str:
    if name != str(name) or surname != str(surname):
        return 'Podaj dane typu string'
    return f'Cześć {name} {surname}!'


x = (typ_tekstowy('Anna', 'Cichoń'))
print(x)

# ZAD 2


def typ_numeryczny(int1: int, int2: int) -> int:
    return int1*int2


print(typ_numeryczny(7, 3))

# ZAD 3


def typ_logiczny(liczba: int) -> bool:
    if liczba % 2 == 0:
        return True
    return False


y = typ_logiczny(5)
print(y)

if y:
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')

# ZAD 4


def wieksza(int1: int, int2: int, int3: int) -> bool:
    return int1 + int2 >= int3


print(wieksza(1, 4, 8))

# ZAD 5


def typ_lista(lista: list, liczba: int) -> bool:
    return liczba in lista


print(typ_lista([1, 2, 3], 2))

# ZAD 6


def laczenie_list(lista1: list, lista2: list) -> list:
    nowa_lista = list(set(lista1 + lista2))
    return [i**3 for i in nowa_lista]


print(laczenie_list([1, 2, 3], [2, 6, 8]))
