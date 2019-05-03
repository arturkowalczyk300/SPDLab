import os
from dataclasses import dataclass

print("SPD Lab 04")

# zmienne poczatkowe

@dataclass
class Zadanie:
    r: float
    p: float
    q: float

l_zadania=[]
liczba_zadan=0
S=[] #wektor rozpoczecia wykonywanych zadan
C=[] #wektor zakonczenia zadan
NN=[]
NG=[]

nazwaKatalogu = "daneLab4"  # od teraz bedzie wczytywac wszystkie instancje z katalogu
l_nazwyPlikow = []

#######global #####################################
# NOWE STRUKTURY
###########################################

m_liczbaZadan = 0
l_czasTrwania = []  # lista zawierajaca czasy trwania na n maszynach (wiec lista dwuwymiarowa)
l_czasZakonczenia = []

wczytane = []


# kolory = ["red", "green", "blue", "cyan", "magenta"]

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

                   #print("r=",r," p=",p," q=",q)
                    l_zadania.append(Zadanie(r,p,q))
                else:
                    ustawienia = [int(s) for s in linia.split() if s.isdigit()]
                    liczba_zadan=ustawienia[0]
                iterator = iterator + 1
    else:
        print("plik nie istnieje!!!")

    wczytane.append(ustawienia)
    wczytane.append(plik_zadania)
    # NOWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE wczytywanie do pliku
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
            max=NG[i].r
            maxindex=i
    return maxindex#zwraca index minimalnej wartosci

def Schrage():
    #inicjalizacja
    global l_zadania
    global NN
    global NG

    N=l_zadania
    NN=N #zadania nieuszeregowane
    NG=[] # zadania gotowe
    t=0 #chwila czasowa #todo: poprawic z zera
    i=1
    RO=[] #tymczasowo lista uszeregowanych zadan

    cmax=0 #todo: change it

    tempIter=0
    while((NG != []) or (NN != [])): #szukanie zadan gotowych do uszeregowania (rj<=t)
        while((NN != []) and (NN[mojeMin()].r <= t)):
            e = mojeMin()
            NG.append(NN[e]) #dodaje do zbioru zadan gotowych
            print("dodaje zadanie")
            del NN[e] #usuwam ze zbioru zadan nieuszeregowanych

        if(NG ==[]): #
            t = NN[mojeMin()].r #najmniejsze r w zestawieniu nieuporzadkowanych
        else:
            j = mojeMax() #index
            RO.append(j+tempIter)
            tempIter+=1
            #k = k +1
            t = t + NG[j].p #dodaje czas trwania wybranego zadania
            del NG[j]
       # cmax = max(cmax,t+ q.e)
    print("     kolejnosc", RO, "cmax", cmax)




# glowna czesc
print("SPDLab 4")
wczytajDaneZFolderu(nazwaKatalogu)

for nazwaPliku in l_nazwyPlikow:
    print("*nazwa przetwarzanego pliku", nazwaPliku)
    wczytajDaneZPlikuSCHRAGE("daneLab4/" + nazwaPliku)
    print(liczba_zadan)
    print(l_zadania)
    Schrage()