import os

print("SPD Lab 04")

# zmienne poczatkowe

cmax = 0
cmax_poprz = 0

nazwaKatalogu = "daneLab4"  # od teraz bedzie wczytywac wszystkie instancje z katalogu
l_nazwyPlikow = []

#######global #####################################
# NOWE STRUKTURY
###########################################


m_liczbaMaszyn = 0
m_liczbaZadan = 0
l_zadania = []
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
    global l_czasTrwania
    m_liczbaMaszyn = wczytane[0][1]
    m_liczbaZadan = wczytane[0][0]

    # przygotowanie rozmiaru struktur danych, WAZNE
    for i in range(0, m_liczbaMaszyn):
        global l_czasTrwania
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
    wczytajDaneZPliku("daneLab4/" + nazwaPliku)
    Schrage()