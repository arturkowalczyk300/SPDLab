import os
import random
import math
import time
print("SPD Lab 03")


nazwaKatalogu = "daneLab3"  # od teraz bedzie wczytywac wszystkie instancje z katalogu
l_nazwyPlikow = []

#######global #####################################
# NOWE STRUKTURY
###########################################
l_czasTrwania = []  # lista zawierajaca czasy trwania na n maszynach (wiec lista dwuwymiarowa)

m_liczbaMaszyn = 0
m_liczbaZadan = 0
l_zadania = []
l_czasTrwania = []  # lista zawierajaca czasy trwania na n maszynach (wiec lista dwuwymiarowa)
l_czasZakonczenia = []

wczytane = []

#neh
posortowana = []

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


def wczytajDaneZFolderu(nazwaFolderu):
    for tempNazwaPliku in os.listdir(nazwaFolderu):
        l_nazwyPlikow.append(tempNazwaPliku)

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

    # przygotowanie rozmiaru struktur danych, WAZNE
    for i in range(0, m_liczbaMaszyn):
        l_czasTrwania.append([])

    for k in range(0, m_liczbaMaszyn):
        templista = []
        for i in range(0, m_liczbaZadan):
            # l_czasTrwania[i]=wczytane[1][i][0]
            templista.append(wczytane[1][i][k])
        l_czasTrwania[k] = templista

    l_zadania = range(1, m_liczbaZadan + 1)
    # print(l_czasTrwania)
    # print("liczba maszyn", m_liczbaMaszyn)

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

def NEHStandardowy():
    l_sumaTrwania = []
    for z in range(0, m_liczbaZadan):
        l_sumaTrwania.append(0)
        for m in range(0, m_liczbaMaszyn):
            l_sumaTrwania[z] += l_czasTrwania[m][z]

    temp = l_sumaTrwania.copy()
    # sortowania czasow trwania #krok2
    for i in range(0, len(l_sumaTrwania)):
        tempmax = max(temp)
        tempindex = temp.index(tempmax)
        temp[temp.index(tempmax)] = -1000000  # zeby powtornie nie znalazlo tej wartosci
        posortowana.append(tempindex + 1)

    global poprzedniaKolejnosc
    global poprzedniCzasZakonczenia
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
            d = przegladKolejnosci(posortowana.index(i) + 1, m_liczbaMaszyn, l1)
            if (m > d):  # wybrane najlepsze zadanie
                m = d
                l3 = l1
        l2 = l3
        poprzedniaKolejnosc = l2.copy()
        poprzedniCzasZakonczenia = l_czasZakonczenia.copy()
    return l2

def symulowaneWyzarzanie():
    #pomiarCzasu=time.clock()

    najgorszyCmax=0
    najlepszyCmax=1000000
    # zmienne poczatkowe
    T = 100000  # aktualna temperatura | inicjowana jako MAX
    Tk = 0.1  # temperatura koncowa
    wsp = 0.99    # wspolczynnik wychladzania
    rnd = 0  # liczba losowa z przedzialu (0,1)
    Fakt = 0  # wartosc funkcji celu(cmax) dla aktualnej permutacji
    Fpoprz = 0  # wartosc funkcji celu dla poprzedniej permutacji
    Fdelta = 0  # roznica funkcji celu (poprzednia minus aktualna)
    P = 0  # prawdopodobienstwo niekorzystnego ruchu
    cmax = 0
    cmax_poprz = 0

    rozwPocz = list(range(0,
                          m_liczbaZadan))  # krok1: wygeneruj rozwiazanie poczatkowe  . w tym przypadku bedzie to kolejnosc naturalna

    #rozwPocz=NEHStandardowy()
    pomiarCzasu = time.clock()

    #print("rozw poczatkowe=", rozwPocz)
    kolejnosc = rozwPocz
    #print("lZadan=", m_liczbaZadan, "kolejnosc=", kolejnosc)
    def zamiana(): #swap
        r=random.choice(kolejnosc)
        r1=random.choice(kolejnosc)
        a, b = kolejnosc.index(r), kolejnosc.index(r1)
        if(a!=b):
            kolejnosc[b], kolejnosc[a] = kolejnosc[a], kolejnosc[b]

    def insert():
        a = random.randrange(0, m_liczbaZadan)
        b = random.randrange(0, m_liczbaZadan)
        kolejnosc.remove(a)
        kolejnosc.insert(b, a)
        return kolejnosc        
    poprzKolejnosc=[]
    while (T > Tk):
        cmax = 0
        cmax_poprz = 0
        # losowy ruch
        # cmax= # przelicz
        #if(poprzKolejnosc==kolejnosc):
            #print("#takie same#", kolejnosc, poprzKolejnosc)
        poprzKolejnosc=kolejnosc
        cmax_poprz=przegladKolejnosci(m_liczbaZadan, m_liczbaMaszyn, kolejnosc)
        zamiana()
        cmax=przegladKolejnosci(m_liczbaZadan, m_liczbaMaszyn, kolejnosc)

        rnd = random.random()  # losuj randa
        #print("#rand#",rnd)
        #wyliczanie prawdopodobienstaw
        if(cmax<cmax_poprz): #rozw lepsze od obecnego
            P=1
        else:
            P=math.exp((cmax_poprz-cmax)/T)
            #print("P",P)
        # P= #wylicz prawdopodobenstwo
        if (P >= rnd):
            x=0
            #print("dobry ruch, akceptuje")
        #elif(P==1): #modyfikacja algorytmu, odrzucam te z P=1
        #    kolejnosc = poprzKolejnosc
        #    cmax = cmax_poprz
        else:
            kolejnosc=poprzKolejnosc
            cmax=cmax_poprz
            #print("slaby ruch, cofam")
        T = T * wsp
        if(cmax<najlepszyCmax):
            najlepszyCmax=cmax
        if(cmax>najgorszyCmax):
            najgorszyCmax=cmax
    print(nazwaPliku, cmax, time.clock()-pomiarCzasu)
    # glowna czesc
print("SPDLab 3")
wczytajDaneZFolderu(nazwaKatalogu)

for nazwaPliku in l_nazwyPlikow:
    #dprint("*nazwa przetwarzanego pliku", nazwaPliku)
    wczytajDaneZPliku("daneLab3/" + nazwaPliku)
    symulowaneWyzarzanie()
print("gotowe")