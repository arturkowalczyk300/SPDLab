# Sterowanie procesami dyskretnymi, laboratorium 1, 2019
# todo (6) - johnson dla 2 maszyn w osobnej funkcji
# todo (8) - naprawa sztywnej kolejnosci w wizualizacji
import matplotlib.pyplot as plt
import numpy as np
import os
import time

## konfiguracja dla 2 maszyn
dwie_zadania = [1, 2, 3, 4, 5]
dwie_czas_na_maszynie_1 = [4, 4, 10, 6, 2]
dwie_czas_na_maszynie_2 = [5, 1, 4, 10, 3]
dwie_liczba_maszyn = 2
dwie_liczba_zadan = len(dwie_zadania)
# inna konfiguracja dla 2 maszyn
# dwie_zadania = [1, 2, 3]
# dwie_czas_na_maszynie_1 = [4, 4, 10]
# dwie_czas_na_maszynie_2 = [5, 1, 4]
# dwie_liczba_maszyn = 2
# dwi#e_liczba_zadan = len(dwie_zadania)

# konfiguracja dla 3 maszyn
trzy_zadania = [1, 2, 3, 4]
trzy_czas_na_maszynie_1 = [5, 4, 4, 3]
trzy_czas_na_maszynie_2 = [5, 5, 4, 5]
trzy_czas_na_maszynie_3 = [3, 2, 5, 7]
trzy_liczba_maszyn = 3

# instancja t000
#trzy_zadania = [1, 2, 3, 4]
#trzy_czas_na_maszynie_1 = [1, 9, 7, 4]
#trzy_czas_na_maszynie_2 = [3, 3, 8, 8]
#trzy_czas_na_maszynie_3 = [8, 5, 6, 7]
#trzy_liczba_maszyn = 3

# sekcja z danymi
kolory = ["red", "green", "blue", "cyan", "magenta"]
zakonczenie_zadan_1 = [0, 0, 0, 0, 0]
zakonczenie_zadan_2 = [0, 0, 0, 0, 0]
zakonczenie_zadan_3 = [0, 0, 0, 0, 0]

wczytane=[]

def wczytajDaneZPliku(nazwaPliku):
    wczytane.clear()
    print("wczytywanie")
    plik_zadania = []
    if os.path.isfile(nazwaPliku):
        with open(nazwaPliku, "r") as tekst:
            iterator = 0
            for linia in tekst:
                linia = linia.replace("\n", "")
                linia = linia.replace("\r", "")
                if iterator != 0:
                    #plik_zadania.append(linia)
                    plik_czasy_trwania=[int(s) for s in linia.split() if s.isdigit()]
                    #print("czasy trwania", plik_czasy_trwania)
                    plik_zadania.append([])
                    plik_zadania[iterator-1]=plik_czasy_trwania.copy()
                else:
                    ustawienia=[int(s) for s in linia.split() if s.isdigit()]
                    plik_liczba_zadan=ustawienia[0]
                    plik_liczba_maszyn=ustawienia[1]
                iterator = iterator + 1
                #print(linia)
        #print("to co ma byc", plik_zadania)
    else:
        print("plik nie istnieje!!!")

    wczytane.append(ustawienia)
    wczytane.append(plik_zadania)
    trzy_zadania=range(1,plik_liczba_zadan+1)
    trzy_liczba_maszyn=plik_liczba_maszyn
    trzy_czas_na_maszynie_1=plik_zadania[0].copy()
    trzy_czas_na_maszynie_2=plik_zadania[1].copy()
    trzy_czas_na_maszynie_3=plik_zadania[2].copy()

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
    for i in range(0, len(arg_kolejnosc) - 1):
        plt.hlines(-1, zakonczenie_zadan_1[arg_kolejnosc[i] - 1], zakonczenie_zadan_1[arg_kolejnosc[i + 1] - 1],
                   colors=kolory[i + 1],
                   lw=4)
    # wizualizacja maszyny drugiej
    for i in range(0, len(czas_na_maszynie_2)):
        plt.hlines(-2, zakonczenie_zadan_2[arg_kolejnosc[i] - 1] - arg_czas_na_maszynie_2[arg_kolejnosc[i] - 1],
                   zakonczenie_zadan_2[arg_kolejnosc[i] - 1], colors=kolory[i], lw=4)

    plt.margins(0.1)
    plt.grid()
    plt.xticks(np.arange(0, 40, 1))
    plt.yticks(np.arange(0, -3, -1))
    plt.text(0, 0, "kolejnosc: " + str(arg_kolejnosc) + " || cmax=" + str(arg_cmax))
    # plt.show()
    plt.savefig(arg_nazwa_pliku)
    plt.close()


def wizualizacjaTrzechMaszyn(arg_czas_na_maszynie_2, arg_czas_na_maszynie_3, arg_kolejnosc,
                             arg_nazwa_pliku, arg_cmax):
    plt.figure(figsize=(20, 7))
    # wizualizacja maszyny pierwszej
    plt.hlines(-1, 0, zakonczenie_zadan_1[arg_kolejnosc[0] - 1], colors=kolory[0], lw=4)
    for i in range(0, len(arg_kolejnosc) - 1):
        plt.hlines(-1, zakonczenie_zadan_1[arg_kolejnosc[i] - 1], zakonczenie_zadan_1[arg_kolejnosc[i + 1] - 1],
                   colors=kolory[i + 1],
                   lw=4)

    # wizualizacja maszyny drugiej
    for i in range(0, len(arg_kolejnosc)):
        plt.hlines(-2, zakonczenie_zadan_2[arg_kolejnosc[i] - 1] - arg_czas_na_maszynie_2[arg_kolejnosc[i] - 1],
                   zakonczenie_zadan_2[arg_kolejnosc[i] - 1], colors=kolory[i], lw=4)

    # wizualizacja maszyny trzeciej
    for i in range(0, len(arg_kolejnosc)):
        plt.hlines(-3, zakonczenie_zadan_3[arg_kolejnosc[i] - 1] - arg_czas_na_maszynie_3[arg_kolejnosc[i] - 1],
                   zakonczenie_zadan_3[arg_kolejnosc[i] - 1], colors=kolory[i], lw=4)

    plt.margins(0.1)
    plt.grid()
    plt.xticks(np.arange(0, 40, 1))
    plt.yticks(np.arange(0, -4, -1))
    plt.text(0, 0, "kolejnosc: " + str(arg_kolejnosc) + " || cmax=" + str(arg_cmax))
    # plt.show()
    plt.savefig(arg_nazwa_pliku)
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


def przegladKolejnosciTrzechMaszyn(n, arg_kolejnosc, arg_czas_na_maszynie_1, arg_czas_na_maszynie_2,
                                   arg_czas_na_maszynie_3):  # n zadan
    for k in range(0, n):
        arg_kolejnosc[k] = arg_kolejnosc[k] - 1  # zmiana indeksowania na zgodne z tablicami (numeracja od zera)
    zakonczenie_zadan_1[arg_kolejnosc[0]] = arg_czas_na_maszynie_1[arg_kolejnosc[0]]  # zaczyna sie w t=0
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
wczytajDaneZPliku("dwie.txt")
print("wcyztane dla 2 maszyn", wczytane)

dwie_zadania=list(range(1,wczytane[0][0]+1))
print("dwiezadania", dwie_zadania)
for i in range(0, wczytane[0][0]):
    dwie_czas_na_maszynie_1[i] = wczytane[1][i][0]
    dwie_czas_na_maszynie_2[i] = wczytane[1][i][1]


zadania = dwie_zadania
czas_na_maszynie_1 = dwie_czas_na_maszynie_1.copy()
czas_na_maszynie_2 = dwie_czas_na_maszynie_2.copy()
liczba_maszyn = dwie_liczba_maszyn
liczba_zadan = len(zadania)
czas = 0
permutacje = []

print("Przeglad zupelny wszystkich permutacji:")
# wyswietla wszystkie permutacje
for p in permutacja(zadania):
    permutacje.append(p)

kolejnosc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # maksymalnie 10 zadan
wykres = 0
mincmax = 10000
najlepszaKolejnosc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for p in permutacje:
    cmax = przegladKolejnosci(dwie_liczba_zadan, p, czas_na_maszynie_1, czas_na_maszynie_2)
    wizualizacjaDwochMaszyn(czas_na_maszynie_2, p, "wykresy/przeglad_zupelny/" + str(wykres), cmax)
    wykres += 1
    if cmax < mincmax:
        mincmax = cmax
        najlepszaKolejnosc = p
    print("kolejnosc=", p, " || cmax=", cmax)

print("1) Najlepsza kolejnosc z przegladu zupelnego:", najlepszaKolejnosc, "cmax", mincmax)
cmax = przegladKolejnosci(dwie_liczba_zadan, najlepszaKolejnosc, czas_na_maszynie_1, czas_na_maszynie_2)
wizualizacjaDwochMaszyn(czas_na_maszynie_2, najlepszaKolejnosc, "wykresy/przeglad_zupelny/najlepszaKolejnosc", mincmax)

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
for k in range(0, len(n)):
    Min1 = min(czas1)
    Min2 = min(czas2)  # znajdujemy zadanie o najkrotszym czasie wykonywania
    index1 = czas1.index(Min1)
    index2 = czas2.index(Min2)
    # teraz musze znalezc indeksy minimow
    if Min1 < Min2:  # jesli najkrotsze bedzie na maszynie1, to dodaj je na poczatek
        l1.append(index1 + 1)
        czas1[index1] = 1000000  # zamiast usuwania
        czas2[index1] = 1000000
    elif Min1 > Min2:  # jesli najkrotsze bedzie na maszynie drugiej to dodaj je na koniec
        l2.insert(0, index2 + 1)
        czas1[index2] = 1000000
        czas2[index2] = 1000000
    elif Min1 == Min2:
        # wycieramy pierwsze zadanie (o mniejszym indeksie_
        if (index1 > index2):
            l2.insert(0, index2 + 1)  # mozna wybrac losowo
            czas1[index2] = 10000000
            czas2[index2] = 10000000
        else:
            l1.append(index1 + 1)
            czas1[index1] = 10000000
            czas2[index1] = 10000000

najkrotsza = l1 + l2
cmax = przegladKolejnosci(dwie_liczba_zadan, najkrotsza, czas_na_maszynie_1, czas_na_maszynie_2)
print("2) Algorytm Johnsona dla 2 maszyn: ", najkrotsza, "cmax=", cmax)
wizualizacjaDwochMaszyn(czas_na_maszynie_2, najkrotsza, "wykresy/Johnson_2maszyny/wykres", cmax)

# wczytaj konfiguracje dla 3 maszyn
wczytajDaneZPliku("trzy.txt")
print("wczytane dla 3 maszyn", wczytane)
trzy_zadania=range(1,wczytane[0][0]+1)
for i in range(0, wczytane[0][0]):
    trzy_czas_na_maszynie_1[i] = wczytane[1][i][0]
    trzy_czas_na_maszynie_2[i] = wczytane[1][i][1]
    trzy_czas_na_maszynie_3[i] = wczytane[1][i][2]

n = trzy_zadania  # zadania
czas1 = trzy_czas_na_maszynie_1.copy()
czas2 = trzy_czas_na_maszynie_2.copy()
czas3 = trzy_czas_na_maszynie_3.copy()
czasw1 = czas1.copy()  # tylko do deklaracji
czasw2 = czas2.copy()  # tylko do deklaracji
for i in range(0, len(czas1)):
    czasw1[i] = czas1[i] + czas2[i]

for i in range(0, len(czas2)):
    czasw2[i] = czas2[i] + czas3[i]

    czasw1Org = czasw1.copy()
    czasw2Org = czasw2.copy()
# czasw1 = (czas1 + czas2)  # laczymy czasy wykonywania sie na maszynach 1 i 2 w jeden czas
# czasw2 = (czas3 + czas2)  # analogicznie dla maszyn 2 i 3
# print("czasw1", czasw1, " |||| czasw2", czasw2)

# w tej chwili mamy obliczone czasy dla dwoch wirtualnych maszyn, wiec mozna uzyc zwyklego algorytmu Johnsona dla dwoch maszyn
a = list(n)  # tworzenie listy do n zadan#
l1 = []  # scheduler1
l2 = []  # scheduler2
najkrotsza = []
for k in range(0, len(n)):
    Min1 = min(czasw1)
    Min2 = min(czasw2)  # znajdujemy zadanie o najkrotszym czasie wykonywania
    index1 = czasw1.index(Min1)
    index2 = czasw2.index(Min2)
    # teraz musze znalezc indeksy minimow
    if Min1 < Min2:  # jesli najkrotsze bedzie na maszynie1, to dodaj je na poczatek
        l1.append(index1 + 1)
        czasw1[index1] = 1000000  # zamiast usuwania
        czasw2[index1] = 1000000
    elif Min1 > Min2:  # jesli najkrotsze bedzie na maszynie drugiej to dodaj je na koniec
        l2.insert(0, index2 + 1)
        czasw1[index2] = 1000000
        czasw2[index2] = 1000000
    elif Min1 == Min2:
        # wycieramy pierwsze zadanie (o mniejszym indeksie_
        if (index1 > index2):
            l2.insert(0, index2 + 1)  # mozna wybrac losowo
            czasw1[index2] = 10000000
            czasw2[index2] = 10000000
        else:
            l1.append(index1 + 1)
            czasw1[index1] = 10000000
            czasw2[index1] = 10000000

czasw1 = czasw1Org
czasw2 = czasw2Org

najkrotsza = l1 + l2
taa = [1, 4, 3, 2]
# najkrotsza = taa
# najkrotsza=[3,4,1,2]
przegladKolejnosci(4, najkrotsza, czasw1, czasw2)
cmax = przegladKolejnosciTrzechMaszyn(4, najkrotsza, trzy_czas_na_maszynie_1, trzy_czas_na_maszynie_2,
                                      trzy_czas_na_maszynie_3)
print("3) Algorytm Johnsona dla 3 maszyn: ", najkrotsza, "cmax=", cmax)
wizualizacjaTrzechMaszyn(trzy_czas_na_maszynie_2, trzy_czas_na_maszynie_3, najkrotsza,
                         'wykresy/Johnson_3maszyny/wykres', cmax)


