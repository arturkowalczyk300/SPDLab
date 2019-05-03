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
cmax = 0
cmax_poprz = 0

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


def Schrage():
    r = [] #termin dostpnosci zadania
    p = l_czasTrwania #czas wykonania zadania
    q = [] #czas dostraczenia zadania
    t = 0 #chwila czasowa
    k = 0 #pozycja w permutacji
    cmax = 0
    kolejnosc = []
    G = [] #zbior zadan gotowych do realizacji
    N = list(range(0, m_liczbaZadan)) #zbior zadan nieuszeregowanych
    def szukajmin():
        j = 0;
        for i in range (N):
            if N[j].r<N[i].r:
                {}
            else:
                j = i
        return j;


    while((G != []) or (N != [])):
        while((N != []) and (min(N.r) <= t)):
            e = min(N.r)
            G = G.append(e)
            N = N.remove(e)
        if(G ==[]):
            t = min(N.r)
        e = max(G.q)
        G = G.remove(e)

        k = k +1
        kolejnosc[k] = e
        t = t + p.e
        cmax = max(cmax,t+ q.e)
    print("     kolejnosc", kolejnosc, "cmax", cmax)




# glowna czesc
print("SPDLab 4")
wczytajDaneZFolderu(nazwaKatalogu)

for nazwaPliku in l_nazwyPlikow:
    print("*nazwa przetwarzanego pliku", nazwaPliku)
    wczytajDaneZPlikuSCHRAGE("daneLab4/" + nazwaPliku)
    print(liczba_zadan)
    print(l_zadania)
    #Schrage()