# Sterowanie procesami dyskretnymi, laboratorium 1, 2019
# todo(1) - refaktoryzacja - mniej wywolan zmienionej kolejnosci
# todo(2) - algorytm johnsona (2) - lepsze wyszukiwanie minimum i iterowanie po petli
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


kolory = ["red", "green", "blue", "cyan", "magenta"]
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
mincmax=10000
najlepszaKolejnosc=[0,0,0,0,0]

for p in permutacje:
    # kolejnosc = p
    kolejnosc = p
    for k in range(0, 5):
        kolejnosc[k] = kolejnosc[k] - 1  # zmiana indeksowania na zgodne z tablicami (numeracja od zera)
    zakonczenie_zadan_1[kolejnosc[0]] = czas_na_maszynie_1[kolejnosc[0]]
    for i in range(1, 5):
        zakonczenie_zadan_1[kolejnosc[i]] = zakonczenie_zadan_1[kolejnosc[i - 1]] + czas_na_maszynie_1[kolejnosc[i]]
    zakonczenie_zadan_2[kolejnosc[0]] = zakonczenie_zadan_1[kolejnosc[0]] + czas_na_maszynie_2[kolejnosc[0]]
    for i in range(1, 5):
        # jesli zadanie i sie zakonczylo na maszynie pierwszej to odpalam je na drugiej. jesli nie, czekam do jego konca.
        if (zakonczenie_zadan_1[kolejnosc[i]] < zakonczenie_zadan_2[
            kolejnosc[i - 1]]):  # jesli zakonczenie zadania nastapilo wczesniej
            zakonczenie_zadan_2[kolejnosc[i]] = zakonczenie_zadan_2[kolejnosc[i - 1]] + czas_na_maszynie_2[
                kolejnosc[i]]
        else:
            zakonczenie_zadan_2[kolejnosc[i]] = zakonczenie_zadan_1[kolejnosc[i]] + czas_na_maszynie_2[kolejnosc[i]]
    cmax = zakonczenie_zadan_2[kolejnosc[4]]
    for k in range(0, 5):
        kolejnosc[k] = kolejnosc[k] + 1  # zmiana indeksowania na naturalne z powrotem
    if cmax < mincmax:
        mincmax = cmax
        najlepszaKolejnosc=kolejnosc
    # wizualizacja maszyny pierwszej
    plt.figure(figsize=(20, 7))
    plt.hlines(-1, 0, zakonczenie_zadan_1[kolejnosc[0] - 1], colors=kolory[0], lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[kolejnosc[0] - 1], zakonczenie_zadan_1[kolejnosc[1] - 1], colors=kolory[1],
               lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[kolejnosc[1] - 1], zakonczenie_zadan_1[kolejnosc[2] - 1], colors=kolory[2],
               lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[kolejnosc[2] - 1], zakonczenie_zadan_1[kolejnosc[3] - 1], colors=kolory[3],
               lw=4)
    plt.hlines(-1, zakonczenie_zadan_1[kolejnosc[3] - 1], zakonczenie_zadan_1[kolejnosc[4] - 1], colors=kolory[4],
               lw=4)
    # wizualizacja maszyny drugiej
    plt.hlines(-2, zakonczenie_zadan_2[kolejnosc[0] - 1] - czas_na_maszynie_2[kolejnosc[0] - 1],
               zakonczenie_zadan_2[kolejnosc[0] - 1], colors=kolory[0], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[kolejnosc[1] - 1] - czas_na_maszynie_2[kolejnosc[1] - 1],
               zakonczenie_zadan_2[kolejnosc[1] - 1], colors=kolory[1], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[kolejnosc[2] - 1] - czas_na_maszynie_2[kolejnosc[2] - 1],
               zakonczenie_zadan_2[kolejnosc[2] - 1], colors=kolory[2], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[kolejnosc[3] - 1] - czas_na_maszynie_2[kolejnosc[3] - 1],
               zakonczenie_zadan_2[kolejnosc[3] - 1], colors=kolory[3], lw=4)
    plt.hlines(-2, zakonczenie_zadan_2[kolejnosc[4] - 1] - czas_na_maszynie_2[kolejnosc[4] - 1],
               zakonczenie_zadan_2[kolejnosc[4] - 1], colors=kolory[4], lw=4)
    plt.margins(0.1)
    plt.grid()
    plt.xticks(np.arange(0, 40, 1))
    plt.yticks(np.arange(0, -3, -1))
    plt.text(0, 0, "kolejnosc: " + str(kolejnosc) + " || cmax=" + str(cmax))
    # plt.show()
    #plt.savefig("wykresy/" + str(wykres))
    wykres += 1
    print("kolejnosc=", p, " || cmax=", cmax, " || uk.1", zakonczenie_zadan_1, " || uk.2", zakonczenie_zadan_2)

print("najlepsza konfiguracja przeplywowego", najlepszaKolejnosc, "cmax", mincmax)


# przykladowa konfiguracja
zadania = [1, 2, 3, 4, 5]
czas_na_maszynie_1 = [4, 4, 10, 6, 2]
czas_na_maszynie_2 = [5, 1, 4, 10, 3]
zakonczenie_zadan_1 = [0, 0, 0, 0, 0]
zakonczenie_zadan_2 = [0, 0, 0, 0, 0]
liczba_maszyn = 2
liczba_zadan = 5
czas = 0

# algorytm Johnsona dla wariantu 2-maszynowego
n = zadania  # zadania
czas1 = czas_na_maszynie_1  # czas zadan na m1
czas2 = czas_na_maszynie_2  # czas zadan na m2
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

# Jeśli obie opcje znajdują się na komputerze 1,
# wybierz najpierw tę z dłuższą operacją 2

# Jeśli oba są na maszynie 2,
# wybierz najpierw tę z dłuższą operacją 1.
print("l1=", l1, " || l2=", l2)
najkrotsza = l1 + l2
print(najkrotsza)

"""
#Algorytm dla 3 maszyn
n #zadania
czas1=[] #czas zadan na m1
czas2=[] #czas zadan na m2
czas3=[] #czas zadan na m3
m1[n,czas1]
m2[n,czas2]
m2[n,czas3]
czasw1=[(czas1+czas2)]
czasw2=[(czas3+czas2)]
mw1=[n, czasw1] #wirtualna maszyna 1
mw2=[n, czasw2] #wirtualna maszyna 2
a=list(1,n) # tworzenie listy do n zadan
l1=[]
l2=[]
najkrotsza=[]
for n in a
Min1 = min(czasw1)
Min2 = min(czaw2)
if Min1 < Min2
a.remove(m1[n,Min1])
l1.append(m1[n,Min1])
elif Min2 < Min1
a.remove(m2[n,Min2])
l2.insert(0,m2[n,Min2])
elif Min1=Min2
a.remove(m1[n,Min1])
l1.append(m1[n,Min1]) #mozna wybrac losowo
Jeśli obie opcje znajdują się na komputerze 1,
 wybierz najpierw tę z dłuższą operacją 2

Jeśli oba są na maszynie 2,
wybierz najpierw tę z dłuższą operacją 1.


najkrotsza = l1 + l2
print(najkrotsza)
"""
