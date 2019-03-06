#Sterowanie procesami dyskretnymi, laboratorium 1, 2019

def permutacja(liczba):
    dlugosc = len(liczba)
    if dlugosc == 1:
        return [liczba]
    elif dlugosc == 0:
        return []
    else:
        wynik = []

        for i in range(dlugosc):
            a = liczba[i]
            b = liczba[:i] + liczba[i+1:]
            for p in permutacja(b):
                wynik.append([a] + p)
        return wynik


lista = [1,2,3]
for p in permutacja(lista):
    print(p)
	