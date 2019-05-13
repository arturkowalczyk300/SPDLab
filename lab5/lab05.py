import os
import time
from dataclasses import dataclass

print("SPD Lab 05")

# zmienne poczatkowe

@dataclass
class Zadanie:
    r: float
    p: float
    q: float
    id: int
    rozpoczecie: float = 0
    zakonczenie:float = 0
l_zadania=[]
liczba_zadan=0
S=[] #wektor rozpoczecia wykonywanych zadan
C=[] #wektor zakonczenia zadan
NN=[]
NG=[]
sigma=[]

nazwaKatalogu = "daneLab5"  # od teraz bedzie wczytywac wszystkie instancje z katalogu
l_nazwyPlikow = []


m_liczbaZadan = 0
l_czasTrwania = []  # lista zawierajaca czasy trwania na n maszynach (wiec lista dwuwymiarowa)
l_czasZakonczenia = []

wczytane = []

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


def wczytajDaneZPlikuSCHRAGE(nazwaPliku):
    global l_zadania
    global liczba_zadan
    l_zadania.clear()
    wczytane.clear()
    plik_zadania = []
    r=0
    p=0
    q=0
    if os.path.isfile(nazwaPliku):
        with open(nazwaPliku, "r") as tekst:
            iterator = 0
            for linia in tekst:
                linia = linia.replace("\n", "")
                linia = linia.replace("\r", "")
                if iterator != 0:
                    plik_rpq = [int(s) for s in linia.split() if s.isdigit()]
                    r=plik_rpq[0]
                    p = plik_rpq[1]
                    q = plik_rpq[2]
                    l_zadania.append(Zadanie(r,p,q, iterator))
                else:
                    ustawienia = [int(s) for s in linia.split() if s.isdigit()]
                    liczba_zadan=ustawienia[0]
                iterator = iterator + 1
    else:
        print("plik nie istnieje!!!")

    wczytane.append(ustawienia)
    wczytane.append(plik_zadania)
    # nowe wczytywanie do pliku
    global m_liczbaMaszyn
    global m_liczbaZadan
    global l_czasTrwania
    m_liczbaMaszyn = wczytane[0][1]
    m_liczbaZadan = wczytane[0][0]

    # przygotowanie rozmiaru struktur danych, WAZNE
    for i in range(0, m_liczbaMaszyn):
        global l_czasTrwania
        l_czasTrwania.append([])

def mojeMin(): #zwraca indeks elementu w NN o najmniejszym r
    global NN
    min=10000000
    minindex=-100
    for i in range(len(NN)):
        if(NN[i].r<min):
            min=NN[i].r
            minindex=i
    return minindex#zwraca index minimalnej wartosci

def mojeMax(): #zwraca indeks elementu w NN o najmniejszym r
    global NG
    max=0
    maxindex=-100
    for i in range(len(NG)):
        if(NG[i].q>max):
            max=NG[i].q
            maxindex=i
    return maxindex#zwraca index minimalnej wartosci

def Schrage():
    #inicjalizacja
    global l_zadania
    global NN
    global NG
    global sigma

    N=l_zadania
    NN=N #zadania nieuszeregowane
    NG=[] # zadania gotowe
    t=0 #chwila czasowa #todo: poprawic z zera
    sigma=[]
    i=1


    cmax=0 #todo: change it

    tempIter=0
    while((NG != []) or (NN != [])): #szukanie zadan gotowych do uszeregowania (rj<=t)
        while((NN != []) and (NN[mojeMin()].r <= t)):
            j = mojeMin()
            NG.append(NN[j]) #dodaje do zbioru zadan gotowych`
            del NN[j] #usuwam ze zbioru zadan nieuszeregowanych
        if(NG ==[]): #brak zadan do uporzadkowania, wiec zwiekszamy chwile czasowa
            t = NN[mojeMin()].r #najmniejsze r w zestawieniu nieuporzadkowanych
        else:
            j = mojeMax() #index
            sigma.append(NG[j]) #dodaje zadanie do wektora kolejnosci !!!
            tempIter+=1
            t = t + NG[j].p #dodaje czas trwania wybranego zadania
            del NG[j]
    liczba=0
    wypelnijRozpoczeciaZadan()
    wypelnijZakonczeniaZadan()
    tempcmax=funkcjaCelu()
    return tempcmax

def Carlier():
    print("carlier")


def wypelnijRozpoczeciaZadan():
    global sigma
    poprzednieZadanie=None
    for zadanie in sigma:
        if(not (poprzednieZadanie is None)):
            zadanie.rozpoczecie=max(zadanie.r, poprzednieZadanie.rozpoczecie + poprzednieZadanie.p)
        poprzednieZadanie = zadanie
def wypelnijZakonczeniaZadan():
    global sigma
    for zadanie in sigma:
        zadanie.zakonczenie=zadanie.rozpoczecie+zadanie.p

def funkcjaCelu():
    global sigma
    max=0
    for zadanie in sigma:
        cmax= zadanie.zakonczenie+zadanie.q
        if(cmax>max):
            max=cmax

    return max

def Schrage_z_przerwaniami():
    #inicjalizacja
    global l_zadania
    global NN
    global NG
    global sigma

    N=l_zadania
    NN=N #zadania nieuszeregowane
    NG=[] # zadania gotowe
    t=0 #chwila czasowa #todo: poprawic z zera
    cmax = 0
    i=1
    l=Zadanie(0,0,999999,0)

    cmax=0 #todo: change it

    tempIter=0
    while((NG != []) or (NN != [])): #szukanie zadan gotowych do uszeregowania (rj<=t)
        while((NN != []) and (NN[mojeMin()].r <= t)):
            j = mojeMin()
            NG.append(NN[j]) #dodaje do zbioru zadan gotowych`
             #usuwam ze zbioru zadan nieuszeregowanych
            if (NN[j].q > l.q):
                l.p = t - NN[j].r
                t = NN[j].r

                if(l.p > 0):
                    NG.append(l)
            del NN[j]
        if(NG ==[]): #brak zadan do uporzadkowania, wiec zwiekszamy chwile czasowa
            t = NN[mojeMin()].r #najmniejsze r w zestawieniu nieuporzadkowanych
        else:
            j = mojeMax() #index
            #k = k +1
            l = NG[j]
            t = t + NG[j].p #dodaje czas trwania wybranego zadania
            cmax = max(cmax, t + NG[j].q)
            del NG[j]
    #print('cmax (z przerwaniami):', cmax)
    return cmax
def srednia(arg_start, arg_stop):
    suma=0
    for a in arg_start:
        suma+=a
    sredni_start=suma/len(arg_start)
    suma = 0
    for b in arg_stop:
        suma += b
    sredni_stop = suma / len(arg_stop)
    return [sredni_start, sredni_stop]
# glowna czesc
print("SPDLab 4")
wczytajDaneZFolderu(nazwaKatalogu)
for nazwaPliku in l_nazwyPlikow:
    print("###########################################################")
    print("*nazwa przetwarzanego pliku", nazwaPliku)
    cmaxSchrage=0
    cmaxPrzerwania=0
    start=[]
    stop=[]
    for i in range(0,1000):
        wczytajDaneZPlikuSCHRAGE("daneLab5/" + nazwaPliku)
        start.append(time.time_ns() / (10**9))
        cmaxSchrage=Schrage()
        stop.append(time.time_ns() / (10**9))
        wczytajDaneZPlikuSCHRAGE("daneLab5/" + nazwaPliku)
    sredniaWartosc=srednia(start,stop)
    print("cmax",cmaxSchrage, "## czas wykonania (srednia z 1000):", sredniaWartosc[1]-sredniaWartosc[0]) #stop - start
    start.clear()
    stop.clear()

    for i in range(0,1000):
        wczytajDaneZPlikuSCHRAGE("daneLab5/" + nazwaPliku)
        start.append(time.time_ns() / (10**9))
        cmaxPrzerwania=Schrage_z_przerwaniami()
        stop.append(time.time_ns() / (10**9))
        wczytajDaneZPlikuSCHRAGE("daneLab5/" + nazwaPliku)
    sredniaWartosc=srednia(start,stop)
    print("cmax (przerwania)=",cmaxPrzerwania,"## czas wykonania (srednia z 1000):", sredniaWartosc[1]-sredniaWartosc[0]) #stop - start
    start.clear()
    stop.clear()
