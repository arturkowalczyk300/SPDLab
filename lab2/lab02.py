# Sterowanie procesami dyskretnymi, laboratorium 2, 2019
# Algorytm NEH


# todo (2): algorytmy w funkcjach

import os
#import matplotlib.pyplot as plt
#import numpy as np
import time

nazwaKatalogu = "daneLab2"  # od teraz bedzie wczytywac wszystkie instancje z katalogu
l_nazwyPlikow = []

#######global #####################################
# NOWE STRUKTURY
###########################################
l_czasTrwania = []  # lista zawierajaca czasy trwania na n maszynach (wiec lista dwuwymiarowa)
l_czasZakonczenia = []

m_liczbaMaszyn = 0
m_liczbaZadan = 0
l_zadania = []

czasNEHStandard = []  # lista czasow wykonania zadan w standardowej metodzie neh
czasNEHZmodyfikowany = []  # lista czasow wykonania zadan w zmodyfikowanej metodzie neh

# krok 1: wyzancz w(j)

# STRUKTURY Z AKCELERACJI!
poprzedniaKolejnosc = []
poprzedniCzasZakonczenia = []

wczytane = []

#kolory = ["red", "green", "blue", "cyan", "magenta"]


def wspolnaCzesc(arg_listaDluzsza, arg_listaKrotsza):
    koniecPodobienstwa = -1
    # print("lista1", arg_listaDluzsza, "lista2", arg_listaKrotsza)
    if ((len(arg_listaKrotsza) > len(arg_listaDluzsza)) or len(arg_listaKrotsza) == 0 or len(arg_listaDluzsza) == 0):
        return 0
    # if(len(arg_listaDluzsza)!=len(arg_listaKrotsza)):
    # print("LISTY MUSZA MIEC TAKA SAMA DLUGOSC")
    # return 0
    for i in range(0, len(arg_listaKrotsza)):
        if (arg_listaDluzsza[i] != arg_listaKrotsza[i]):
            koniecPodobienstwa = i
            break
    if (koniecPodobienstwa == -1):  # jesli wartosc nie zostala przypisana
        koniecPodobienstwa = len(arg_listaKrotsza)

    # if (koniecPodobienstwa != 0):
    #    print("#MATCH#: czesc wspolna: ", arg_listaKrotsza[0:koniecPodobienstwa])
    # print("KONIEC PODOBIENSTWA",koniecPodobienstwa)
    return koniecPodobienstwa

'''
def usunStareWykresy():
    folder = "wykresy"
    for plik in os.listdir(folder):
        sciezka = os.path.join(folder, plik)
        try:
            if os.path.isfile(sciezka):
                os.unlink(sciezka)
        except Exception as e:
            print(e)

'''
def wczytajDaneZFolderu(nazwaFolderu):
    for tempNazwaPliku in os.listdir(nazwaFolderu):
        l_nazwyPlikow.append(tempNazwaPliku)


'''def wizualizacja(arg_liczbaZadan, arg_liczbaMaszyn, arg_kolejnosc, arg_nazwa_pliku):
    plt.figure(figsize=(20, 7))
    # wizualizacja maszyny pierwszej
    plt.hlines(-1, 0, l_czasZakonczenia[0][arg_kolejnosc[0] - 1], colors=kolory[0], lw=4)
    for i in range(0, len(arg_kolejnosc) - 1):
        plt.hlines(-1, l_czasZakonczenia[0][arg_kolejnosc[i] - 1], l_czasZakonczenia[0][arg_kolejnosc[i + 1] - 1],
                   colors=kolory[(i + 1) % 5],
                   lw=4)

    liczbaMaszyn = arg_liczbaMaszyn
    for k in range(1, liczbaMaszyn):
        # wizualizacja maszyny drugiej i kazdej kolejnej
        for i in range(0, len(arg_kolejnosc)):
            plt.hlines(-k - 1, l_czasZakonczenia[k][arg_kolejnosc[i] - 1] - l_czasTrwania[k][arg_kolejnosc[i] - 1],
                       l_czasZakonczenia[k][arg_kolejnosc[i] - 1], colors=kolory[i % 5], lw=4)

    plt.margins(0.1)
    plt.grid()
    plt.xticks(np.arange(0, 40, 1))
    plt.yticks(np.arange(0, -3, -1))
    # plt.text(0, 0, "kolejnosc: " + str(arg_kolejnosc) + " || cmax=" + str(arg_cmax))
    # plt.show()
    plt.savefig("wykresy/" + arg_nazwa_pliku)
    plt.close()

'''
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
    # NOWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE wczytywanie do pliku
    l_zadania = list(range(1, wczytane[0][0] + 1))
    global m_liczbaMaszyn
    global m_liczbaZadan
    m_liczbaMaszyn = wczytane[0][1]
    m_liczbaZadan = wczytane[0][0]
    l_czasZakonczenia.clear()  # TODO: a
    l_czasZakonczenia.clear()  # TODO: b
    # przygotowanie rozmiaru struktur danych, WAZNE
    for i in range(0, m_liczbaMaszyn):
        l_czasTrwania.append([])
        l_czasZakonczenia.append([])

    for k in range(0, m_liczbaMaszyn):
        templista = []
        for i in range(0, m_liczbaZadan):
            # l_czasTrwania[i]=wczytane[1][i][0]
            templista.append(wczytane[1][i][k])
        l_czasTrwania[k] = templista

    l_zadania = range(1, m_liczbaZadan + 1)
    # print(l_czasTrwania)
    # print("liczba maszyn", m_liczbaMaszyn)


# liczenie Cmax

def przegladKolejnosci(arg_liczbaZadan, arg_liczbaMaszyn, arg_kolejnosc):  # n zadan
    global poprzedniaKolejnosc
    global poprzedniCzasZakonczenia
    # sprawdz wspolna czesc
    # if (set(arg_kolejnosc) & set(poprzedniaKolejnosc)):
    #    print("#WPSOLNA CZESC#", set(arg_kolejnosc) & set(poprzedniaKolejnosc))]
    l_czasZakonczenia.clear()

    # utworzenie listy do czasu zakonczenia
    for i in range(0, arg_liczbaMaszyn):
        l_czasZakonczenia.append([])
        l_czasZakonczenia[i] = [None] * m_liczbaZadan
        # l_czasZakonczenia[i] = [None] * arg_liczbaZadan


    for k in range(0, arg_liczbaZadan):
        arg_kolejnosc[k] = arg_kolejnosc[k] - 1  # zmiana indeksowania na zgodne z tablicami (numeracja od zera)

    # pierwsza maszyna
      # gdy nie znaleziono czesci wspolnej
        l_czasZakonczenia[0][arg_kolejnosc[0]] = l_czasTrwania[0][arg_kolejnosc[0]]  # zaczyna sie w t=0

    for i in range(1, arg_liczbaZadan):
        l_czasZakonczenia[0][arg_kolejnosc[i]] = l_czasZakonczenia[0][arg_kolejnosc[i - 1]] + \
                                                 l_czasTrwania[0][arg_kolejnosc[i]]

    # kolejne maszyny
    liczbaMaszyn = arg_liczbaMaszyn
    for k in range(1, liczbaMaszyn):
        l_czasZakonczenia[k][arg_kolejnosc[0]] = l_czasZakonczenia[k - 1][arg_kolejnosc[0]] + l_czasTrwania[k][
            arg_kolejnosc[0]]
        for i in range(1, arg_liczbaZadan):
            # jesli zadanie i sie zakonczylo na maszynie pierwszej to zalaczam je na drugiej. jesli nie, czekam do jego konca.
            if (l_czasZakonczenia[k - 1][arg_kolejnosc[i]] < l_czasZakonczenia[k][
                arg_kolejnosc[i - 1]]):  # jesli zakonczenie zadania nastapilo wczesniej
                l_czasZakonczenia[k][arg_kolejnosc[i]] = l_czasZakonczenia[k][arg_kolejnosc[i - 1]] + \
                                                         l_czasTrwania[k][
                                                             arg_kolejnosc[i]]
            else:
                l_czasZakonczenia[k][arg_kolejnosc[i]] = l_czasZakonczenia[k - 1][arg_kolejnosc[i]] + \
                                                         l_czasTrwania[k][arg_kolejnosc[i]]

    ret_cmax = l_czasZakonczenia[arg_liczbaMaszyn - 1][arg_kolejnosc[arg_liczbaZadan - 1]]

    for k in range(0, arg_liczbaZadan):  # juz niepotrzebne
        arg_kolejnosc[k] = arg_kolejnosc[k] + 1  # zmiana indeksowania na naturalne z powrotem
    # poprzedniaKolejnosc = arg_kolejnosc.copy()
    # poprzedniCzasZakonczenia = l_czasZakonczenia.copy()

    return ret_cmax


def NEHStandardowy(check):
    global poprzedniaKolejnosc
    global poprzedniCzasZakonczenia
    start = time.clock()
    l1 = []  # kolejnosc biezaca
    l2 = []  #
    l3 = []
    m = 11111111111111111
    for i in posortowana:
        m = 11111111111111111
        # print("#Wstawiana cyfra#", i)
        for j in range(0, posortowana.index(i) + 1):
            l1 = []
            l1 = l1 + l2
            l1.insert(j, i)  # kolejnosc   #krok3,4
            # print("nana=", l1)
            # print("d1", posortowana.index(i)+1, "d2", len(l1))
            d = przegladKolejnosci(posortowana.index(i) + 1, m_liczbaMaszyn, l1)
            if (m > d):  # wybrane najlepsze zadanie
                m = d
                l3 = l1
                # print("m",m)

        l2 = l3
        # print("najlepsza kolejnosc", l2)
        # print("=========================")
        poprzedniaKolejnosc = l2.copy()
        poprzedniCzasZakonczenia = l_czasZakonczenia.copy()
    end = time.clock()
    total = end - start
    print("Czas : ", "{0:02f}s".format(total))
    print("--Najlepsza kolejnosc NEH = ", l2)
    print("--Cmax NEH = ", m)
    # wizualizacja(m_liczbaZadan, m_liczbaMaszyn, l2, nazwaPliku.replace(".txt","")+"neh.png")
    czasNEHStandard.append(total)  # todo: moze to przetworzyc bo pewnie jest w ms


def NEH_IR4():
    #global poprzedniaKolejnosc
    #global poprzedniCzasZakonczenia
    start = time.clock()
    l1 = []  # kolejnosc biezaca
    l2 = []  #
    l3 = []
    najgorsze = 0
    m = 11111111111111111
    for i in posortowana:
        m = 11111111111111111
        # print("#Wstawiana cyfra#", i)
        for j in range(0, posortowana.index(i) + 1):
            l1 = []
            l1 = l1 + l2
            l1.insert(j, i)  # kolejnosc   #krok3,4

            # print("nana=", l1)
            # print("d1", posortowana.index(i)+1, "d2", len(l1))
            d = przegladKolejnosci(posortowana.index(i) + 1, m_liczbaMaszyn, l1)
            if (m > d):  # wybrane najlepsze zadanie
                m = d
                l3 = l1
        l2 = l3

        if (posortowana.index(i) > 0):

            m = 100000000
            for r in range(0, posortowana.index(i)+ 1):
                if (l2[r] != i):
                    a = l2[r]
                    l2.remove(a)

                    d = przegladKolejnosci(posortowana.index(i), m_liczbaMaszyn, l2)
                    if (d < m):
                        m = d
                        najgorsze = a
                    l2.insert(r,a)

            l2.remove(najgorsze)


            m=1111111111111
            for j in range(0, posortowana.index(i) + 1):
                l1 = []
                l1 = l1 + l2
                l1.insert(j, najgorsze) # kolejnosc   #krok3,4
                #print("l1", l1)
                d = przegladKolejnosci(posortowana.index(i) +1 , m_liczbaMaszyn, l1)
                if (m > d):  # wybrane najlepsze zadanie
                    m = d
                    l3 = l1

        l2 = l3
        #print("najlepsza kolejnosc", l2)
    print("=========================")
        #poprzedniaKolejnosc = l2.copy()
        #poprzedniCzasZakonczenia = l_czasZakonczenia.copy()
    end = time.clock()
    total = end - start
    print("Czas : ", "{0:02f}s".format(total))
    print("--Najlepsza kolejnosc NEH IR4 = ", l2)
    print("--Cmax NEH z modyfikacja IR4= ", m)
    # wizualizacja(m_liczbaZadan, m_liczbaMaszyn, l2, nazwaPliku.replace(".txt","")+"neh.png")
    #czasNEHStandard.append(total)  # todo: moze to przetworzyc bo pewnie jest w ms
# glowna czesc
print("SPDLab 2")
#usunStareWykresy()
wczytajDaneZFolderu(nazwaKatalogu)

for nazwaPliku in l_nazwyPlikow:
    print("#####Plik: ", nazwaPliku, "##############################################################")
    # wczytywanie do pliku
    wczytajDaneZPliku("daneLab2/" + nazwaPliku)

    # w(j) = suma czasow 2 maszyn
    print("liczba maszyn", m_liczbaMaszyn)
    czas1 = l_czasTrwania[0].copy()
    czas2 = l_czasTrwania[1].copy()
    czas_wszystkich_zadan_2 = czas1.copy()

    for i in range(0, len(czas1)):
        czas_wszystkich_zadan_2[i] = czas1[i] + czas2[i]
    # sortowanie zadań majejąco po w(j) przy 2 maszynach
    a = l_zadania  # tworzenie listy do n zadan#
    posortowana = []

    # tworzenie wektora zsumowanych czasow trwania   #krok 1
    l_sumaTrwania = []
    for z in range(0, m_liczbaZadan):
        l_sumaTrwania.append(0)
        for m in range(0, m_liczbaMaszyn):
            l_sumaTrwania[z] += l_czasTrwania[m][z]

    # print("Suma czasow trwania", l_sumaTrwania)

    posortowana = []
    temp = l_sumaTrwania.copy()
    # sortowania czasow trwania #krok2
    for i in range(0, len(l_sumaTrwania)):
        tempmax = max(temp)
        tempindex = temp.index(tempmax)
        temp[temp.index(tempmax)] = -1000000  # zeby powtornie nie znalazlo tej wartosci
        posortowana.append(tempindex + 1)

    # print("posortowana lista", posortowana)

    # for k in range(0, m_liczbaZadan):
    #     Max2 = max(czas_wszystkich_zadan_2)
    #     index2 = czas_wszystkich_zadan_2.index(Max2)
    #     posortowana.append(index2 + 1)
    #     czas_wszystkich_zadan_2[index2] = 0
    cmax = przegladKolejnosci(m_liczbaZadan, m_liczbaMaszyn, posortowana)
    # print("--Posortowana lista dla", m_liczbaMaszyn,  "maszyn: ", posortowana)
    print("--Cmax = ", cmax)
    print("-------------------------------------------------------------------------------------------")
    # wizualizacja(m_liczbaZadan, m_liczbaMaszyn, posortowana, nazwaPliku.replace(".txt","")+".png")

    # funkcja testujaca
    # cmax10=przegladKolejnosci(1, m_liczbaMaszyn, [2])
    # print("UDALO SIE")
    # liczenie cmax wedlug algorytmu NEH
    print("Algorytm NEH")
    NEHStandardowy("")
    NEH_IR4()
# NEHZmodyfikowany()
print("czas standard []s: calkowity", sum(czasNEHStandard), " poszczegolne", czasNEHStandard)
print("czas zmodyfkowanego algorytmu calk", sum(czasNEHStandard), "poszczegolne", czasNEHZmodyfikowany)
print("koniec programu!")