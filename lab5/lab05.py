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

def mojeMin(NN): #zwraca indeks elementu w NN o najmniejszym r

    min=10000000
    minindex=-100
    for i in range(len(NN)):
        if(NN[i].r<min):
            min=NN[i].r
            minindex=i
    return minindex#zwraca index minimalnej wartosci

def mojeMax(NG): #zwraca indeks elementu w NN o najmniejszym r
    max=0
    maxindex=-100
    for i in range(len(NG)):
        if(NG[i].q>max):
            max=NG[i].q
            maxindex=i
    return maxindex#zwraca index minimalnej wartosci


def Schrage(l_zadania):
    #inicjalizacja
    NN=[]
    NG=[]
    sigma=[]

    N=l_zadania.copy()
    NN=N #zadania nieuszeregowane
    NG=[] # zadania gotowe
    t=0 #chwila czasowa #todo: poprawic z zera
    sigma=[]
    i=1


    cmax=0 #todo: change it

    tempIter=0
    while((NG != []) or (NN != [])): #szukanie zadan gotowych do uszeregowania (rj<=t)
        while((NN != []) and (NN[mojeMin(NN)].r <= t)):
            j = mojeMin(NN)
            NG.append(NN[j]) #dodaje do zbioru zadan gotowych`
            del NN[j] #usuwam ze zbioru zadan nieuszeregowanych
        if(NG ==[]): #brak zadan do uporzadkowania, wiec zwiekszamy chwile czasowa
            t = NN[mojeMin(NN)].r #najmniejsze r w zestawieniu nieuporzadkowanych
        else:
            j = mojeMax(NG) #index
            sigma.append(NG[j]) #dodaje zadanie do wektora kolejnosci !!!
            tempIter+=1
            t = t + NG[j].p #dodaje czas trwania wybranego zadania
            del NG[j]
    liczba=0
    wypelnijRozpoczeciaZadan(sigma)
    wypelnijZakonczeniaZadan(sigma)
    tempcmax=funkcjaCelu(sigma)

    return [tempcmax, sigma]


def znajdzOstatnieZadanieNaSciezceKrytycznej(sigma):
    #print("szukam ostatniego zadania na sciezce")
    print()
    maxIndex=-100
    for i in range(0,len(l_zadania)):
        a=funkcjaCelu(sigma)
        b=sigma[i].zakonczenie
        c=sigma[i].q
        print("i",i,"a=",a,"b=",b,"c=",c, "suma", b+c)
        #if(funkcjaCelu(sigma)==l_zadania[i].zakonczenie + l_zadania[i].q):
        if (a == b+c):
            maxIndex=i
    print("znalezione maxindex", maxIndex)
    return maxIndex
def znajdzPierwszeZadanieNaSciezceKrytycznej(l_zadania,sigma):
    #print("szukam pierwszego zadania na sciezce")
    b=0

def znajdzZadanieKrytyczne(l_zadania):
    c=0

def Carlier(l_zadania):
    print("carlier")
    N=l_zadania
    UB=0 #gorne oszacowanie wartosci funkcji celu - dla najlepszego dotychczas rozwiazania
    LB=0 #dolne oszacowanie wartosci funkcji celu
    PI_ST=[] #optymalna permutacja wykonania zadan na maszynie
    PI=[] #permutacja wykonania zadan na maszynie
    U=0 #wartosc funkcji celu

    temp=Schrage(l_zadania) #[0] - cmax    [1]-kolejnosc
    PI=temp[1]
    U=temp[0]
    if(U<UB):
        UB=U
        PI_ST=PI

    #tempblok

    #wybor zadan
    b=znajdzOstatnieZadanieNaSciezceKrytycznej(PI)
    a=znajdzPierwszeZadanieNaSciezceKrytycznej(l_zadania,PI)
    c=znajdzZadanieKrytyczne(l_zadania)

    if(c==0):
        return PI_ST


def wypelnijRozpoczeciaZadan(sigma):
    poprzednieZadanie=None
    for zadanie in sigma:
        if(not (poprzednieZadanie is None)):
            zadanie.rozpoczecie=max(zadanie.r, poprzednieZadanie.rozpoczecie + poprzednieZadanie.p)
        poprzednieZadanie = zadanie
def wypelnijZakonczeniaZadan(sigma):
    for zadanie in sigma:
        zadanie.zakonczenie=zadanie.rozpoczecie+zadanie.p

def funkcjaCelu(sigma):
    max=0
    for zadanie in sigma:
        cmax= zadanie.zakonczenie+zadanie.q
        if(cmax>max):
            max=cmax

    return max

def Schrage_z_przerwaniami(l_zadania):
    #inicjalizacja
    NN=[]
    NG=[]
    sigma=[]

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
        while((NN != []) and (NN[mojeMin(NN)].r <= t)):
            j = mojeMin(NN)
            NG.append(NN[j]) #dodaje do zbioru zadan gotowych`
             #usuwam ze zbioru zadan nieuszeregowanych
            if (NN[j].q > l.q):
                l.p = t - NN[j].r
                t = NN[j].r

                if(l.p > 0):
                    NG.append(l)
            del NN[j]
        if(NG ==[]): #brak zadan do uporzadkowania, wiec zwiekszamy chwile czasowa
            t = NN[mojeMin(NN)].r #najmniejsze r w zestawieniu nieuporzadkowanych
        else:
            j = mojeMax(NG) #index
            #k = k +1
            sigma.append(NG[j])
            l = NG[j]
            t = t + NG[j].p #dodaje czas trwania wybranego zadania
            cmax = max(cmax, t + NG[j].q)
            del NG[j]
    #print('cmax (z przerwaniami):', cmax)
    return [cmax, sigma]
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
    print("cmax schrage", Schrage(l_zadania.copy()))

    wczytajDaneZPlikuSCHRAGE("daneLab5/" + nazwaPliku)
    Carlier(l_zadania)
