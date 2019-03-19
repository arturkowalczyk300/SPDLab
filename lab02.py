# Sterowanie procesami dyskretnymi, laboratorium 2, 2019
# Algorytm NEH

#TODO (1): dzialajace dynamiczne struktury danych dla dwoch maszyn
#TODO (2): dzialajace dynamiczne struktury danych dla trzech maszyn
#TODO (3): przerobka przegladu kolejnosci na n
#TODO (4): wszystko dynamicznie i na n

import os

dwie_nazwaPliku = "dwie.txt"
trzy_nazwaPliku = "trzy.txt"

############################################
# NOWE STRUKTURY
###########################################
l_czasTrwania = []  # lista zawierajaca czasy trwania na n maszynach (wiec lista dwuwymiarowa)
l_czasZakonczenia = []
m_liczbaMaszyn=0
l_zadania=[]
# krok 1: wyzancz w(j)

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
    #NOWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE wczytywanie do pliku
    l_zadania = list(range(1, wczytane[0][0] + 1))
    m_liczbaMaszyn = wczytane[0][0]
    #przygotowanie rozmiaru struktur danych, WAZNE
    for i in range(0,m_liczbaMaszyn):
        l_czasTrwania.append([])
        l_czasZakonczenia.append([])

    for i in range(0, m_liczbaMaszyn):
        l_czasTrwania[i]=wczytane[1][i][0]

# liczenie Cmax
def przegladKolejnosci(n, arg_kolejnosc, arg_czas_na_maszynie_1, arg_czas_na_maszynie_2):  # n zadan
    for k in range(0, n):
        arg_kolejnosc[k] = arg_kolejnosc[k] - 1  # zmiana indeksowania na zgodne z tablicami (numeracja od zera)
    l_czasZakonczenia[0][arg_kolejnosc[0]] = arg_czas_na_maszynie_1[arg_kolejnosc[0]]
    for i in range(1, n):
        l_czasZakonczenia[0][arg_kolejnosc[i]] = l_czasZakonczenia[0][arg_kolejnosc[i - 1]] + \
                                                 arg_czas_na_maszynie_1[arg_kolejnosc[i]]
    l_czasZakonczenia[1][arg_kolejnosc[0]] = l_czasZakonczenia[0][arg_kolejnosc[0]] + arg_czas_na_maszynie_2[
        arg_kolejnosc[0]]
    for i in range(1, n):
        # jesli zadanie i sie zakonczylo na maszynie pierwszej to zalaczam je na drugiej. jesli nie, czekam do jego konca.
        if (l_czasZakonczenia[0][arg_kolejnosc[i]] < l_czasZakonczenia[1][
            arg_kolejnosc[i - 1]]):  # jesli zakonczenie zadania nastapilo wczesniej
            l_czasZakonczenia[1][arg_kolejnosc[i]] = l_czasZakonczenia[1][arg_kolejnosc[i - 1]] + \
                                                     arg_czas_na_maszynie_2[
                                                         arg_kolejnosc[i]]
        else:
            l_czasZakonczenia[1][arg_kolejnosc[i]] = l_czasZakonczenia[0][arg_kolejnosc[i]] + \
                                                     arg_czas_na_maszynie_2[arg_kolejnosc[i]]
    ret_cmax = l_czasZakonczenia[1][arg_kolejnosc[n - 1]]
    for k in range(0, n):
        arg_kolejnosc[k] = arg_kolejnosc[k] + 1  # zmiana indeksowania na naturalne z powrotem
    return ret_cmax


def przegladKolejnosciTrzechMaszyn(n, arg_kolejnosc):  # n zadan
    for k in range(0, n):
        arg_kolejnosc[k] = arg_kolejnosc[k] - 1  # zmiana indeksowania na zgodne z tablicami (numeracja od zera)
    l_czasZakonczenia[0][arg_kolejnosc[0]] = l_czasTrwania[0][arg_kolejnosc[0]]  # zaczyna sie w t=0
    for i in range(1, n):
        l_czasZakonczenia[0][arg_kolejnosc[i]] = l_czasZakonczenia[0][arg_kolejnosc[i - 1]] + \
                                                 l_czasTrwania[0][arg_kolejnosc[i]]
    l_czasZakonczenia[1][arg_kolejnosc[0]] = l_czasZakonczenia[0][arg_kolejnosc[0]] + l_czasTrwania[1][
        arg_kolejnosc[0]]
    for i in range(1, n):
        # jesli zadanie i sie zakonczylo na maszynie pierwszej to zalaczam je na drugiej. jesli nie, czekam do jego konca.
        if (l_czasZakonczenia[0][arg_kolejnosc[i]] < l_czasZakonczenia[1][
            arg_kolejnosc[i - 1]]):  # jesli zakonczenie zadania nastapilo wczesniej
            l_czasZakonczenia[1][arg_kolejnosc[i]] = l_czasZakonczenia[1][arg_kolejnosc[i - 1]] + \
                                                     l_czasTrwania[1][
                                                         arg_kolejnosc[i]]
        else:
            l_czasZakonczenia[1][arg_kolejnosc[i]] = l_czasZakonczenia[0][arg_kolejnosc[i]] + \
                                                     l_czasTrwania[1][arg_kolejnosc[i]]

    ############
    l_czasZakonczenia[2][arg_kolejnosc[0]] = l_czasZakonczenia[1][arg_kolejnosc[0]] + l_czasTrwania[2][
        arg_kolejnosc[0]]
    for i in range(1, n):
        # jesli zadanie i sie zakonczylo na maszynie pierwszej to odpalam je na drugiej. jesli nie, czekam do jego konca.
        if (l_czasZakonczenia[1][arg_kolejnosc[i]] < l_czasZakonczenia[2][
            arg_kolejnosc[i - 1]]):  # jesli zakonczenie zadania nastapilo wczesniej
            l_czasZakonczenia[2][arg_kolejnosc[i]] = l_czasZakonczenia[2][arg_kolejnosc[i - 1]] + \
                                                     l_czasTrwania[2][
                                                         arg_kolejnosc[i]]
        else:
            l_czasZakonczenia[2][arg_kolejnosc[i]] = l_czasZakonczenia[1][arg_kolejnosc[i]] + \
                                                     l_czasTrwania[2][arg_kolejnosc[i]]

    ret_cmax = l_czasZakonczenia[2][arg_kolejnosc[n - 1]]

    for k in range(0, n):
        arg_kolejnosc[k] = arg_kolejnosc[k] + 1  # zmiana indeksowania na naturalne z powrotem
    return ret_cmax


# wczytywanie do pliku
wczytajDaneZPliku("daneLab2/" + dwie_nazwaPliku)

# w(j) = suma czasow 2 maszyn
n = m_liczbaMaszyn
czas1 = l_czasTrwania[0].copy()
czas2 = l_czasTrwania[1].copy()
czas_wszystkich_zadan_2 = czas1.copy()

for i in range(0, len(czas1)):
    czas_wszystkich_zadan_2[i] = czas1[i] + czas2[i]
# sortowanie zadań majejąco po w(j) przy 2 maszynach
a = list(n)  # tworzenie listy do n zadan#
posortowana = []

for k in range(0, len(n)):
    Max2 = max(czas_wszystkich_zadan_2)
    index2 = czas_wszystkich_zadan_2.index(Max2)
    posortowana.append(index2 + 1)
    czas_wszystkich_zadan_2[index2] = 0
cmax = przegladKolejnosci(m_liczbaMaszyn, posortowana)
print("Posortowana lista dla 2 maszyn: ", posortowana)
print("Cmax = ", cmax)

# # liczenie cmax wedlug algorytmu NEH dla 2 maszyn
# l1 = []
# l2 = []
# l3 = []
# m = 11111
# for i in posortowana:
#     m = 1111
#     for j in range(0, posortowana.index(i) + 1):
#         l1 = []
#         l1 = l1 + l2
#         l1.insert(j, i)
#         print("nana=", l1)
#         d = przegladKolejnosci(posortowana.index(i) + 1, l1, trzy_czas_na_maszynie_1,
#                                trzy_czas_na_maszynie_2)
#         if (m > d):
#             m = d
#             l3 = l1
#             print(m)
#     l2 = l3
#
# print("Najlepsza kolejnosc = ", l2)
# print("Cmax = ", m)
#
# # wczytanie do pliku
# wczytajDaneZPliku("daneLab2/" + trzy_nazwaPliku)
# trzy_zadania = range(1, wczytane[0][0] + 1)
# for i in range(0, wczytane[0][0]):
#     trzy_czas_na_maszynie_1[i] = wczytane[1][i][0]
#     trzy_czas_na_maszynie_2[i] = wczytane[1][i][1]
#     trzy_czas_na_maszynie_3[i] = wczytane[1][i][2]
#
# # w(j) = suma czasow 3 maszyn
#
# n = trzy_zadania
# czas1 = trzy_czas_na_maszynie_1.copy()
# czas2 = trzy_czas_na_maszynie_2.copy()
# czas3 = trzy_czas_na_maszynie_3.copy()
# czas_wszystkich_zadan_3 = czas1.copy()
# for i in range(0, len(czas1)):
#     czas_wszystkich_zadan_3[i] = czas1[i] + czas2[i] + czas3[i]
# # sortowanie zadań majejąco po w(j) przy 3 maszynach
# a = list(n)  # tworzenie listy do n zadan#
# posortowana = []
#
# for k in range(0, len(n)):
#     Max3 = max(czas_wszystkich_zadan_3)
#     index3 = czas_wszystkich_zadan_3.index(Max3)
#     posortowana.append(index3 + 1)
#     czas_wszystkich_zadan_3[index3] = 0
#
# print("Posortowana lista dla 3 maszyn: ", posortowana)
#
# cmax3 = przegladKolejnosciTrzechMaszyn(len(trzy_zadania), posortowana, trzy_czas_na_maszynie_1, trzy_czas_na_maszynie_2,
#                                        trzy_czas_na_maszynie_3)
# print("Cmax=", cmax3)
#
# # liczenie cmax wedlug algorytmu NEH dla 3 maszyn
# l1 = []
# l2 = []
# l3 = []
# m = 11111
# for i in posortowana:
#     m = 1111
#     for j in range(0, posortowana.index(i) + 1):
#         l1 = []
#         l1 = l1 + l2
#         l1.insert(j, i)
#         print("nana=", l1)
#         d = przegladKolejnosciTrzechMaszyn(posortowana.index(i) + 1, l1, trzy_czas_na_maszynie_1,
#                                            trzy_czas_na_maszynie_2, trzy_czas_na_maszynie_3)
#         if (m > d):
#             m = d
#             l3 = l1
#             print(m)
#     l2 = l3
#
# print("Najlepsza kolejnosc = ", l2)
# print("Cmax = ", m)
