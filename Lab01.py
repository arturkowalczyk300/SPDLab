# Sterowanie procesami dyskretnymi, laboratorium 1, 2019
# todo(3) - wizualizacje dla 3 maszyn
# todo (6) - johnson dla 2 maszyn w osobnej funkcji
# todo(7) - liczenie cmax dla 3 maszyn
# todo (8) - naprawa sztywnej kolejnosci w wizualizacji
import matplotlib.pyplot as plt
import numpy as np
import time

# konfiguracja dla 2 maszyn
dwie_zadania = [1, 2, 3, 4, 5]
dwie_czas_na_maszynie_1 = [4, 4, 10, 6, 2]
dwie_czas_na_maszynie_2 = [5, 1, 4, 10, 3]
dwie_liczba_maszyn = 2

# konfiguracja dla 3 maszyn
# trzy_zadania = [1, 2, 3, 4]
# trzy_czas_na_maszynie_1 = [5, 4, 4, 3]
# trzy_czas_na_maszynie_2 = [5, 5, 4, 5]
# trzy_czas_na_maszynie_3 = [3, 2, 5, 7]
# trzy_liczba_maszyn = 3

# instancja t000
trzy_zadania = [1, 2, 3, 4]
trzy_czas_na_maszynie_1 = [1, 9, 7, 4]
trzy_czas_na_maszynie_2 = [3, 3, 8, 8]
trzy_czas_na_maszynie_3 = [8, 5, 6, 7]
trzy_liczba_maszyn = 3

# sekcja z danymi
kolory = ["red", "green", "blue", "cyan", "magenta"]
zakonczenie_zadan_1 = [0, 0, 0, 0, 0]
zakonczenie_zadan_2 = [0, 0, 0, 0, 0]
zakonczenie_zadan_3 = [0, 0, 0, 0, 0]

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


def wizualizacjaDwochMaszyn(arg_czas_na_maszynie_2, arg_kolejnosc,
                            arg_nazwa_pliku, arg_cmax):
    plt.figure(figsize=(20, 7))
    # wizualizacja maszyny pierwszej
    plt.hlines(-1, 0, zakonczenie_zadan_1[arg_kolejnosc[0] - 1], colors=kolory[0], lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[arg_kolejnosc[0] - 1], zakonczenie_zadan_1[arg_kolejnosc[1] - 1],
               colors=kolory[1],
               lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[arg_kolejnosc[1] - 1], zakonczenie_zadan_1[arg_kolejnosc[2] - 1],
               colors=kolory[2],
               lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[arg_kolejnosc[2] - 1], zakonczenie_zadan_1[arg_kolejnosc[3] - 1],
               colors=kolory[3],
               lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[arg_kolejnosc[3] - 1], zakonczenie_zadan_1[arg_kolejnosc[4] - 1],
               colors=kolory[4],
               lw=4)
    # wizualizacja maszyny drugiej
    plt.hlines(-2, zakonczenie_zadan_2[arg_kolejnosc[0] - 1] - arg_czas_na_maszynie_2[arg_kolejnosc[0] - 1],
               zakonczenie_zadan_2[arg_kolejnosc[0] - 1], colors=kolory[0], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[arg_kolejnosc[1] - 1] - arg_czas_na_maszynie_2[arg_kolejnosc[1] - 1],
               zakonczenie_zadan_2[arg_kolejnosc[1] - 1], colors=kolory[1], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[arg_kolejnosc[2] - 1] - arg_czas_na_maszynie_2[arg_kolejnosc[2] - 1],
               zakonczenie_zadan_2[arg_kolejnosc[2] - 1], colors=kolory[2], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[arg_kolejnosc[3] - 1] - arg_czas_na_maszynie_2[arg_kolejnosc[3] - 1],
               zakonczenie_zadan_2[arg_kolejnosc[3] - 1], colors=kolory[3], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[arg_kolejnosc[4] - 1] - arg_czas_na_maszynie_2[arg_kolejnosc[4] - 1],
               zakonczenie_zadan_2[arg_kolejnosc[4] - 1], colors=kolory[4], lw=4)
    plt.margins(0.1)
    plt.grid()
    plt.xticks(np.arange(0, 40, 1))
    plt.yticks(np.arange(0, -3, -1))
    plt.text(0, 0, "kolejnosc: " + str(arg_kolejnosc) + " || cmax=" + str(arg_cmax))
    # plt.show()
    plt.savefig("wykresy/" + str(arg_nazwa_pliku))
    plt.close()


def wizualizacjaTrzechMaszyn(arg_czas_na_maszynie_2,arg_czas_na_maszynie_3, arg_kolejnosc,
                             arg_nazwa_pliku, arg_cmax):
    plt.figure(figsize=(20, 7))
    # wizualizacja maszyny pierwszej
    plt.hlines(-1, 0, zakonczenie_zadan_1[arg_kolejnosc[0] - 1], colors=kolory[0], lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[arg_kolejnosc[0] - 1], zakonczenie_zadan_1[arg_kolejnosc[1] - 1],
               colors=kolory[1],
               lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[arg_kolejnosc[1] - 1], zakonczenie_zadan_1[arg_kolejnosc[2] - 1],
               colors=kolory[2],
               lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[arg_kolejnosc[2] - 1], zakonczenie_zadan_1[arg_kolejnosc[3] - 1],
               colors=kolory[3],
               lw=4)

    # wizualizacja maszyny drugiej
    plt.hlines(-2, zakonczenie_zadan_2[arg_kolejnosc[0] - 1] - arg_czas_na_maszynie_2[arg_kolejnosc[0] - 1],
               zakonczenie_zadan_2[arg_kolejnosc[0] - 1], colors=kolory[0], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[arg_kolejnosc[1] - 1] - arg_czas_na_maszynie_2[arg_kolejnosc[1] - 1],
               zakonczenie_zadan_2[arg_kolejnosc[1] - 1], colors=kolory[1], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[arg_kolejnosc[2] - 1] - arg_czas_na_maszynie_2[arg_kolejnosc[2] - 1],
               zakonczenie_zadan_2[arg_kolejnosc[2] - 1], colors=kolory[2], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[arg_kolejnosc[3] - 1] - arg_czas_na_maszynie_2[arg_kolejnosc[3] - 1],
               zakonczenie_zadan_2[arg_kolejnosc[3] - 1], colors=kolory[3], lw=4)

    #wizualizacja maszyny trzeciej
    plt.hlines(-3, zakonczenie_zadan_3[arg_kolejnosc[0] - 1] - arg_czas_na_maszynie_3[arg_kolejnosc[0] - 1],
               zakonczenie_zadan_3[arg_kolejnosc[0] - 1], colors=kolory[0], lw=4)
    plt.hlines(-3, zakonczenie_zadan_3[arg_kolejnosc[1] - 1] - arg_czas_na_maszynie_3[arg_kolejnosc[1] - 1],
               zakonczenie_zadan_3[arg_kolejnosc[1] - 1], colors=kolory[1], lw=4)
    plt.hlines(-3, zakonczenie_zadan_3[arg_kolejnosc[2] - 1] - arg_czas_na_maszynie_3[arg_kolejnosc[2] - 1],
               zakonczenie_zadan_3[arg_kolejnosc[2] - 1], colors=kolory[2], lw=4)
    plt.hlines(-3, zakonczenie_zadan_3[arg_kolejnosc[3] - 1] - arg_czas_na_maszynie_3[arg_kolejnosc[3] - 1],
               zakonczenie_zadan_3[arg_kolejnosc[3] - 1], colors=kolory[3], lw=4)

    plt.margins(0.1)
    plt.grid()
    plt.xticks(np.arange(0, 40, 1))
    plt.yticks(np.arange(0, -4, -1))
    plt.text(0, 0, "kolejnosc: " + str(arg_kolejnosc) + " || cmax=" + str(arg_cmax))
    # plt.show()
    plt.savefig("wykresy/" + str(arg_nazwa_pliku))
    plt.close()


def przegladKolejnosci(n, arg_kolejnosc, arg_czas_na_maszynie_1, arg_czas_na_maszynie_2):  # n zadan
    for k in range(0, n):
        arg_kolejnosc[k] = arg_kolejnosc[k] - 1  # zmiana indeksowania na zgodne z tablicami (numeracja od zera)
    zakonczenie_zadan_1[arg_kolejnosc[0]] = arg_czas_na_maszynie_1[arg_kolejnosc[0]]
    for i in range(1, n):
        zakonczenie_zadan_1[arg_kolejnosc[i]] = zakonczenie_zadan_1[arg_kolejnosc[i - 1]] + \
                                                arg_czas_na_maszynie_1[arg_kolejnosc[i]]
    zakonczenie_zadan_2[arg_kolejnosc[0]] = zakonczenie_zadan_1[arg_kolejnosc[0]] + arg_czas_na_maszynie_2[
        arg_kolejnosc[0]]
    for i in range(1, n):
        # jesli zadanie i sie zakonczylo na maszynie pierwszej to odpalam je na drugiej. jesli nie, czekam do jego konca.
        if (zakonczenie_zadan_1[arg_kolejnosc[i]] < zakonczenie_zadan_2[
            arg_kolejnosc[i - 1]]):  # jesli zakonczenie zadania nastapilo wczesniej
            zakonczenie_zadan_2[arg_kolejnosc[i]] = zakonczenie_zadan_2[arg_kolejnosc[i - 1]] + \
                                                    arg_czas_na_maszynie_2[
                                                        arg_kolejnosc[i]]
        else:
            zakonczenie_zadan_2[arg_kolejnosc[i]] = zakonczenie_zadan_1[arg_kolejnosc[i]] + \
                                                    arg_czas_na_maszynie_2[arg_kolejnosc[i]]
    ret_cmax = zakonczenie_zadan_2[arg_kolejnosc[n - 1]]
    for k in range(0, n):
        arg_kolejnosc[k] = arg_kolejnosc[k] + 1  # zmiana indeksowania na naturalne z powrotem
    return ret_cmax


def przegladKolejnosciTrzechMaszyn(n, arg_kolejnosc, arg_czas_na_maszynie_1, arg_czas_na_maszynie_2, arg_czas_na_maszynie_3):  # n zadan
    for k in range(0, n):
        arg_kolejnosc[k] = arg_kolejnosc[k] - 1  # zmiana indeksowania na zgodne z tablicami (numeracja od zera)
    zakonczenie_zadan_1[arg_kolejnosc[0]] = arg_czas_na_maszynie_1[arg_kolejnosc[0]] #zaczyna sie w t=0
    for i in range(1, n):
        zakonczenie_zadan_1[arg_kolejnosc[i]] = zakonczenie_zadan_1[arg_kolejnosc[i - 1]] + \
                                                arg_czas_na_maszynie_1[arg_kolejnosc[i]]
    zakonczenie_zadan_2[arg_kolejnosc[0]] = zakonczenie_zadan_1[arg_kolejnosc[0]] + arg_czas_na_maszynie_2[
        arg_kolejnosc[0]]
    for i in range(1, n):
        # jesli zadanie i sie zakonczylo na maszynie pierwszej to odpalam je na drugiej. jesli nie, czekam do jego konca.
        if (zakonczenie_zadan_1[arg_kolejnosc[i]] < zakonczenie_zadan_2[
            arg_kolejnosc[i - 1]]):  # jesli zakonczenie zadania nastapilo wczesniej
            zakonczenie_zadan_2[arg_kolejnosc[i]] = zakonczenie_zadan_2[arg_kolejnosc[i - 1]] + \
                                                    arg_czas_na_maszynie_2[
                                                        arg_kolejnosc[i]]
        else:
            zakonczenie_zadan_2[arg_kolejnosc[i]] = zakonczenie_zadan_1[arg_kolejnosc[i]] + \
                                                    arg_czas_na_maszynie_2[arg_kolejnosc[i]]

    ############
    zakonczenie_zadan_3[arg_kolejnosc[0]] = zakonczenie_zadan_2[arg_kolejnosc[0]] + arg_czas_na_maszynie_3[
        arg_kolejnosc[0]]
    for i in range(1, n):
        # jesli zadanie i sie zakonczylo na maszynie pierwszej to odpalam je na drugiej. jesli nie, czekam do jego konca.
        if (zakonczenie_zadan_2[arg_kolejnosc[i]] < zakonczenie_zadan_3[
            arg_kolejnosc[i - 1]]):  # jesli zakonczenie zadania nastapilo wczesniej
            zakonczenie_zadan_3[arg_kolejnosc[i]] = zakonczenie_zadan_3[arg_kolejnosc[i - 1]] + \
                                                    arg_czas_na_maszynie_3[
                                                        arg_kolejnosc[i]]
        else:
            zakonczenie_zadan_3[arg_kolejnosc[i]] = zakonczenie_zadan_2[arg_kolejnosc[i]] + \
                                                    arg_czas_na_maszynie_3[arg_kolejnosc[i]]

    ret_cmax = zakonczenie_zadan_3[arg_kolejnosc[n - 1]]
    for k in range(0, n):
        arg_kolejnosc[k] = arg_kolejnosc[k] + 1  # zmiana indeksowania na naturalne z powrotem
    return ret_cmax

# wczytaj konfiguracje dla dwoch maszyn
zadania = dwie_zadania
czas_na_maszynie_1 = dwie_czas_na_maszynie_1.copy()
czas_na_maszynie_2 = dwie_czas_na_maszynie_2.copy()
liczba_maszyn = dwie_liczba_maszyn
liczba_zadan = len(zadania)
czas = 0
permutacje = []

# wyswietla wszystkie permutacje
for p in permutacja(zadania):
    permutacje.append(p)

kolejnosc = [0, 0, 0, 0, 0]
wykres = 0
mincmax = 10000
najlepszaKolejnosc = [0, 0, 0, 0, 0]

for p in permutacje:
    cmax = przegladKolejnosci(5, p, czas_na_maszynie_1, czas_na_maszynie_2)
    wizualizacjaDwochMaszyn(czas_na_maszynie_2, p, wykres, cmax)
    wykres += 1
    if cmax < mincmax:
        mincmax = cmax
        najlepszaKolejnosc = p
    print("kolejnosc=", p, " || cmax=", cmax)

print("1) Najlepsza kolejnosc z przegladu zupelnego:", najlepszaKolejnosc, "cmax", mincmax)

# algorytm Johnsona dla wariantu 2-maszynowego
n = zadania  # zadania
czas1 = czas_na_maszynie_1.copy()  # czas zadan na m1
czas2 = czas_na_maszynie_2.copy()  # czas zadan na m2
m1 = n  # zadania na maszynie1
m2 = n  # zadania na maszynie2
a = list(n)  # tworzenie listy do n zadan
l1 = []  # scheduler1
l2 = []  # scheduler2
najkrotsza = []
for k in a:
    Min1 = czas1[0]
    Min2 = czas2[0]  # znajdujemy zadanie o najkrotszym czasie wykonywania
    if Min1 < Min2:  # jesli najkrotsze bedzie na maszynie1, to dodaj je na poczatek
        l1.append(k)
        czas1.remove(Min1)
        czas2.remove(Min2)
    elif Min1 > Min2:  # jesli najkrotsze bedzie na maszynie drugiej to dodaj je na koniec
        l2.insert(0, k)
        czas1.remove(Min1)
        czas2.remove(Min2)
    elif Min1 == Min2:
        l1.insert(0, k)  # mozna wybrac losowo
        czas1.remove(Min1)
        czas2.remove(Min2)

najkrotsza = l1 + l2
print("2) Algorytm Johnsona dla 2 maszyn: ", najkrotsza, "cmax=",
      przegladKolejnosci(5, najkrotsza, czas_na_maszynie_1, czas_na_maszynie_2))

# wczytaj konfiguracje dla 3 maszyn
n = trzy_zadania  # zadania
czas1 = trzy_czas_na_maszynie_1.copy()
czas2 = trzy_czas_na_maszynie_2.copy()
czas3 = trzy_czas_na_maszynie_3.copy()
czasw1 = (czas1 + czas2)  # laczymy czasy wykonywania sie na maszynach 1 i 2 w jeden czas
czasw2 = (czas3 + czas2)  # analogicznie dla maszyn 2 i 3
# print("czasw1", czasw1, " |||| czasw2", czasw2)

# w tej chwili mamy obliczone czasy dla dwoch wirtualnych maszyn, wiec mozna uzyc zwyklego algorytmu Johnsona dla dwoch maszyn
a = list(n)  # tworzenie listy do n zadan#
l1 = []  # scheduler1
l2 = []  # scheduler2
najkrotsza = []
for k in a:
    Min1 = czasw1[0]
    Min2 = czasw2[0]  # znajdujemy zadanie o najkrotszym czasie wykonywania
    if Min1 < Min2:  # jesli najkrotsze bedzie na maszynie1, to dodaj je na poczatek
        l1.append(k)
        czasw1.remove(Min1)
        czasw2.remove(Min2)
    elif Min1 > Min2:  # jesli najkrotsze bedzie na maszynie drugiej to dodaj je na koniec
        l2.insert(0, k)
        czasw1.remove(Min1)
        czasw2.remove(Min2)
    elif Min1 == Min2:
        l1.insert(0, k)  # mozna wybrac losowo
        czasw1.remove(Min1)
        czasw2.remove(Min2)

# najkrotsza = l1 + l2
taa = [1, 4, 3, 2]
najkrotsza = taa
print("3) Algorytm Johnsona dla 3 maszyn: ", najkrotsza, "cmax=", przegladKolejnosci(4, najkrotsza, czasw1, czasw2))
przegladKolejnosciTrzechMaszyn(4, najkrotsza, trzy_czas_na_maszynie_1, trzy_czas_na_maszynie_2, trzy_czas_na_maszynie_3)
print("czas na maszynie 1", trzy_czas_na_maszynie_1, "czas na maszynie 2", trzy_czas_na_maszynie_2, "zakonczenie zadan 1", zakonczenie_zadan_1, "zakonczenie zadan 2", zakonczenie_zadan_2)
wizualizacjaTrzechMaszyn(trzy_czas_na_maszynie_2, trzy_czas_na_maszynie_3, najkrotsza, 'XD', 100)
