# Sterowanie procesami dyskretnymi, laboratorium 1, 2019
#todo (1): poprawne kolejnosc kolorow

import matplotlib.pyplot as plt
import numpy as np


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


kolory=["red", "green", "blue", "cyan", "magenta"]
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
wykres = 0
# permutacje.clear()
# permutacje.append([1, 2, 3, 4, 5])
for p in permutacje:
    # kolejnosc = p
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

    # wizualizacja maszyny pierwszej
    plt.figure(figsize=(20, 7))
    plt.hlines(-1, 0, zakonczenie_zadan_1[kolejnosc[0]-1], colors=kolory[0], lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[kolejnosc[0]-1], zakonczenie_zadan_1[kolejnosc[1]-1], colors=kolory[1], lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[kolejnosc[1]-1], zakonczenie_zadan_1[kolejnosc[2]-1], colors=kolory[2], lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[kolejnosc[2]-1], zakonczenie_zadan_1[kolejnosc[3]-1], colors=kolory[3], lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[kolejnosc[3]-1], zakonczenie_zadan_1[kolejnosc[4]-1], colors=kolory[4], lw=4)
    # wizualizacja maszyny drugiej
    plt.hlines(-2, zakonczenie_zadan_2[kolejnosc[0]-1] - czas_na_maszynie_2[kolejnosc[0]-1], zakonczenie_zadan_2[kolejnosc[0]-1],colors=kolory[0], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[kolejnosc[1]-1] - czas_na_maszynie_2[kolejnosc[1]-1], zakonczenie_zadan_2[kolejnosc[1]-1], colors=kolory[1], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[kolejnosc[2]-1] - czas_na_maszynie_2[kolejnosc[2]-1], zakonczenie_zadan_2[kolejnosc[2]-1], colors=kolory[2], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[kolejnosc[3]-1] - czas_na_maszynie_2[kolejnosc[3]-1], zakonczenie_zadan_2[kolejnosc[3]-1], colors=kolory[3], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[kolejnosc[4]-1] - czas_na_maszynie_2[kolejnosc[4]-1], zakonczenie_zadan_2[kolejnosc[4]-1], colors=kolory[4], lw=4)

    plt.margins(0.1)
    plt.grid()
    plt.xticks(np.arange(0, 40, 1))
    plt.yticks(np.arange(0, -3, -1))
    plt.text(0, 0, "kolejnosc: " + str(kolejnosc) + " || cmax=" + str(cmax))
    # plt.show()
    plt.savefig("wykresy/" + str(wykres))
    wykres += 1
    # sprawdzenie czasow ukonczenia - do znalezienia wadliwej konfiguracji
    max1 = 0
    max2 = 0
    wadliwe = 0
    for i in range(0, 5):
        if (zakonczenie_zadan_1[kolejnosc[i] - 1] > max1):
            max1 = zakonczenie_zadan_1[kolejnosc[i] - 1]
        else:
            print("#WADLIWA KONFIGURACJA#", p, "czas konca 1", zakonczenie_zadan_1)
            wadliwe = 1
    for i in range(0, 5):
        if (zakonczenie_zadan_2[kolejnosc[i] - 1] > max2):
            max1 = zakonczenie_zadan_1[kolejnosc[i] - 1]
        else:
            print("#WADLIWA KONFIGURACJA#", p, "czas konca 1", zakonczenie_zadan_2)
            wadliwe = 1

    if (wadliwe == 0):
        print("kolejnosc=", p, " || cmax=", cmax, " || uk.1", zakonczenie_zadan_1, " || uk.2", zakonczenie_zadan_2)
# print("czasy zakonczenia na maszynie 1", zakonczenie_zadan_1)
# print("czasy zakonczenia na maszynie 2", zakonczenie_zadan_2)
print("ZAKONCZENIE", zakonczenie_zadan_1)
