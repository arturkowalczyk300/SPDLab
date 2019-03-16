# Sterowanie procesami dyskretnymi, laboratorium 2, 2019
#Algorytm NEH
import os
dwie_nazwaPliku="dwie.txt"
trzy_nazwaPliku="trzy.txt"

#krok 1: wyzancz w(j)

# inicjalizacja struktur danych dla 2 maszyn
dwie_zadania = [10000, 10000, 10000, 10000]
dwie_czas_na_maszynie_1 = [10, 20, 2, 1, 0, 0, 0,0 ,0 ,0] #maksymalnie 10 zadan || TODO (1): dynamiczna alokacja rozmiaru tablicy
dwie_czas_na_maszynie_2 = [10, 18, 3, 3, 0, 0, 0,0 ,0 ,0] #maksymalnie 10 zadan
dwie_liczba_maszyn = 2
dwie_liczba_zadan = len(dwie_zadania)

# inicjalizacja struktur danych dla 3 maszyn
trzy_zadania = [1000, 1000, 1000, 1000]
trzy_czas_na_maszynie_1 = [1, 7, 6, 8, 0, 0, 0,0 ,0 ,0]
trzy_czas_na_maszynie_2 = [6, 12, 3, 1, 0, 0, 0,0 ,0 ,0]
trzy_czas_na_maszynie_3 = [4, 11, 8, 18, 0, 0, 0,0 ,0 ,0]
trzy_liczba_maszyn = 3

zakonczenie_zadan_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zakonczenie_zadan_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zakonczenie_zadan_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


wczytane = []

def wczytajDaneZPliku(nazwaPliku):
    wczytane.clear()
    plik_zadania = []
    if os.path.isfile(nazwaPliku):
        with open(nazwaPliku, "r") as tekst:
            iterator = 0
            for linia in tekst:
                linia = linia.replace("\n", "")
                linia = linia.replace("\r", "")
                if iterator != 0:
                    plik_czasy_trwania = [int(s) for s in linia.split() if s.isdigit()]
                    plik_zadania.append([])
                    plik_zadania[iterator - 1] = plik_czasy_trwania.copy()
                else:
                    ustawienia = [int(s) for s in linia.split() if s.isdigit()]
                    plik_liczba_zadan = ustawienia[0]
                    plik_liczba_maszyn = ustawienia[1]
                iterator = iterator + 1
    else:
        print("plik nie istnieje!!!")

    wczytane.append(ustawienia)
    wczytane.append(plik_zadania)
    trzy_zadania = range(1, plik_liczba_zadan + 1)
    trzy_liczba_maszyn = plik_liczba_maszyn
    trzy_czas_na_maszynie_1 = plik_zadania[0].copy()
    trzy_czas_na_maszynie_2 = plik_zadania[1].copy()
    trzy_czas_na_maszynie_3 = plik_zadania[2].copy()


#liczenie Cmax
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
        # jesli zadanie i sie zakonczylo na maszynie pierwszej to zalaczam je na drugiej. jesli nie, czekam do jego konca.
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
        zakonczenie_zadan_1 [arg_kolejnosc[i]] = zakonczenie_zadan_1[arg_kolejnosc[i - 1]] + \
                                                arg_czas_na_maszynie_1[arg_kolejnosc[i]]
    zakonczenie_zadan_2[arg_kolejnosc[0]] = zakonczenie_zadan_1[arg_kolejnosc[0]] + arg_czas_na_maszynie_2[
        arg_kolejnosc[0]]
    for i in range(1, n):
        # jesli zadanie i sie zakonczylo na maszynie pierwszej to zalaczam je na drugiej. jesli nie, czekam do jego konca.
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

#wczytywanie do pliku
wczytajDaneZPliku("daneLab2/"+dwie_nazwaPliku)
dwie_zadania = list(range(1, wczytane[0][0] + 1))
for i in range(0, wczytane[0][0]):
    dwie_czas_na_maszynie_1[i] = wczytane[1][i][0]
    dwie_czas_na_maszynie_2[i] = wczytane[1][i][1]
dwie_liczba_zadan = wczytane[0][0]



# w(j) = suma czasow 2 maszyn
n = dwie_zadania
czas1 = dwie_czas_na_maszynie_1.copy()
czas2 = dwie_czas_na_maszynie_2.copy()
czas_wszystkich_zadan_2 = czas1.copy()

for i in range(0, len(czas1)):
    czas_wszystkich_zadan_2[i] = czas1[i] + czas2[i]
#sortowanie zadań majejąco po w(j) przy 2 maszynach
a = list(n)  # tworzenie listy do n zadan#
posortowana=[]

for k in range(0, len(n)):
    Max2 = max(czas_wszystkich_zadan_2)
    index2 = czas_wszystkich_zadan_2.index(Max2)
    posortowana.append(index2 + 1)
    czas_wszystkich_zadan_2[index2] = 0
cmax = przegladKolejnosci(dwie_liczba_zadan, posortowana, dwie_czas_na_maszynie_1, dwie_czas_na_maszynie_2)
print("Posortowana lista dla 2 maszyn: ",posortowana)
print("Cmax = ",cmax)


#liczenie cmax wedlug algorytmu NEH dla 2 maszyn
l1=[]
l2=[]
l3=[]
m=11111
for i in posortowana:
    m=1111
    for j in range(0, posortowana.index(i)+1):
     l1=[]
     l1=l1+l2
     l1.insert(j,i)
     print("nana=",l1)
     d = przegladKolejnosci(posortowana.index(i)+1, l1, trzy_czas_na_maszynie_1,
                                    trzy_czas_na_maszynie_2)
     if(m > d):
         m = d
         l3 = l1
         print(m)
    l2 = l3

print("Najlepsza kolejnosc = ",l2)
print("Cmax = ",m)



#wczytanie do pliku
wczytajDaneZPliku("daneLab2/"+trzy_nazwaPliku)
trzy_zadania = range(1, wczytane[0][0] + 1)
for i in range(0, wczytane[0][0]):
    trzy_czas_na_maszynie_1[i] = wczytane[1][i][0]
    trzy_czas_na_maszynie_2[i] = wczytane[1][i][1]
    trzy_czas_na_maszynie_3[i] = wczytane[1][i][2]



#w(j) = suma czasow 3 maszyn

n = trzy_zadania
czas1 = trzy_czas_na_maszynie_1.copy()
czas2 = trzy_czas_na_maszynie_2.copy()
czas3 = trzy_czas_na_maszynie_3.copy()
czas_wszystkich_zadan_3 = czas1.copy()
for i in range(0, len(czas1)):
    czas_wszystkich_zadan_3[i] = czas1[i] + czas2[i] + czas3[i]
#sortowanie zadań majejąco po w(j) przy 3 maszynach
a = list(n)  # tworzenie listy do n zadan#
posortowana=[]

for k in range(0, len(n)):
    Max3 = max(czas_wszystkich_zadan_3)
    index3 = czas_wszystkich_zadan_3.index(Max3)
    posortowana.append(index3 + 1)
    czas_wszystkich_zadan_3[index3] = 0

print("Posortowana lista dla 3 maszyn: ",posortowana)

cmax3 = przegladKolejnosciTrzechMaszyn(len(trzy_zadania), posortowana, trzy_czas_na_maszynie_1, trzy_czas_na_maszynie_2,
                                      trzy_czas_na_maszynie_3)
print("Cmax=", cmax3)


#liczenie cmax wedlug algorytmu NEH dla 3 maszyn
l1=[]
l2=[]
l3=[]
m=11111
for i in posortowana:
    m=1111
    for j in range(0, posortowana.index(i)+1):
     l1=[]
     l1=l1+l2
     l1.insert(j,i)
     print("nana=",l1)
     d = przegladKolejnosciTrzechMaszyn(posortowana.index(i)+1, l1, trzy_czas_na_maszynie_1,
                                    trzy_czas_na_maszynie_2, trzy_czas_na_maszynie_3)
     if(m > d):
         m = d
         l3 = l1
         print(m)
    l2 = l3

print("Najlepsza kolejnosc = ",l2)
print("Cmax = ",m)
