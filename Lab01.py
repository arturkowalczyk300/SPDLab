# Sterowanie procesami dyskretnymi, laboratorium 1, 2019


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
            b = liczba[:i] + liczba[i + 1:]
            for p in permutacja(b):
                wynik.append([a] + p)
        return wynik


# przykladowa konfiguracja
zadania = [1, 2, 3, 4, 5]
czas_na_maszynie_1 = [4, 4, 10, 6, 2]
czas_na_maszynie_2 = [5, 1, 4, 10, 3]
zakonczenie_zadan_1 = [0, 0, 0, 0, 0]
zakonczenie_zadan_2 = [0, 0, 0, 0, 0]
liczba_maszyn = 2
liczba_zadan = 5
czas = 0

permutacje = []

# wyswietla wszystkie permutacje
for p in permutacja(zadania):
    permutacje.append(p)
    #   print(p)

# print(permutacje)
# naturalna kolejnosc (1,2,3,4,5)
naturalnakolejnosc = [0, 1, 2, 3, 4]
kolejnosc = [0, 0, 0, 0, 0]
for p in permutacje:
    kolejnosc = p
    for k in range(0, 5):
        kolejnosc[k] = kolejnosc[k] - 1  # zmiana indeksowania na zgodne z tablicami (numeracja od zera)

    zakonczenie_zadan_1[kolejnosc[0]] = czas_na_maszynie_1[kolejnosc[0]]
    for i in range(1, 5):
        # print("i=", i)
        zakonczenie_zadan_1[kolejnosc[i]] = zakonczenie_zadan_1[kolejnosc[i - 1]] + czas_na_maszynie_1[kolejnosc[i]]

    zakonczenie_zadan_2[kolejnosc[0]] = zakonczenie_zadan_1[kolejnosc[0]] + czas_na_maszynie_2[kolejnosc[0]]
    for i in range(1, 5):
        # jesli zadanie i sie zakonczylo na maszynie pierwszej to odpalam je na drugiej. jesli nie, czekam do jego konca.
        if (zakonczenie_zadan_1[kolejnosc[i]] < zakonczenie_zadan_2[
            kolejnosc[i - 1]]):  # jesli zakonczenie zadania nastapilo wczesniej
            zakonczenie_zadan_2[kolejnosc[i]] = zakonczenie_zadan_2[kolejnosc[i - 1]] + czas_na_maszynie_2[kolejnosc[i]]
        else:
            zakonczenie_zadan_2[kolejnosc[i]] = zakonczenie_zadan_1[kolejnosc[i]] + czas_na_maszynie_2[kolejnosc[i]]
    cmax = zakonczenie_zadan_2[kolejnosc[4]]
    for k in range(0, 5):
        kolejnosc[k] = kolejnosc[k] + 1  # zmiana indeksowania na naturalne z powrotem
    print("kolejnosc=", p, "cmax=", cmax)

# print("czasy zakonczenia na maszynie 1", zakonczenie_zadan_1)
# print("czasy zakonczenia na maszynie 2", zakonczenie_zadan_2)
