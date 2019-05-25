import os
import time
from dataclasses import dataclass

print("SPD Lab 05")
carliercmax=0
znalezionoOptymalneRozwiazanie=False
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
prawidlowy_wynik=0

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
    global prawidlowy_wynik
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
                if iterator >1:
                    plik_rpq = [int(s) for s in linia.split() if s.isdigit()]
                    r=plik_rpq[0]
                    p = plik_rpq[1]
                    q = plik_rpq[2]
                    l_zadania.append(Zadanie(r,p,q, iterator))
                elif iterator==1:
                    ustawienia = [int(s) for s in linia.split() if s.isdigit()]
                    liczba_zadan=ustawienia[0]
                else: ##pierwsza linia - prawidlowy wynik
                    prawidlowy_wynik=int(linia.split()[0])
                    #print("prawidlowy", prawidlowy_wynik)
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
    max=-100
    maxindex=-100
    for i in range(len(NG)):
        if(NG[i].q>max):
            max=NG[i].q
            maxindex=i
    return maxindex#zwraca index minimalnej wartosci


def Schrage(arg_l_zadania):
    #inicjalizacja
    NN=[]
    NG=[]
    sigma=[]

    N=arg_l_zadania.copy()
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
            #print("dbg: j=",j, "len(NG)=", len(NG))
            sigma.append(NG[j]) #dodaje zadanie do wektora kolejnosci !!!
            tempIter+=1
            t = t + NG[j].p #dodaje czas trwania wybranego zadania
            del NG[j]
            #print("Udalo sie usunac!")
    liczba=0
    wypelnijRozpoczeciaZadan(sigma)
    wypelnijZakonczeniaZadan(sigma)
    global tempcmax
    tempcmax=funkcjaCelu(sigma)
    return [tempcmax, sigma]


def znajdzOstatnieZadanieNaSciezceKrytycznej(sigma):
    #print()
    maxIndex=-100
    for i in range(0,len(sigma)):
        a=funkcjaCelu(sigma)
        b=sigma[i].zakonczenie
        c=sigma[i].q
        if (a == b+c):
            maxIndex=i
    return maxIndex
def znajdzPierwszeZadanieNaSciezceKrytycznej(sigma, IndeksOstatniegoZadania):
    maxIndex = -100
    for i in range(0, len(sigma)):
        cmax=funkcjaCelu(sigma)
        a = sigma[i].r
        b = 0
        for s in range(i, IndeksOstatniegoZadania+1):
            b+=sigma[s].p

        c = sigma[IndeksOstatniegoZadania].q
        if (cmax== a + b + c):
            maxIndex = i
    if(maxIndex==-100):
        return 0
    return maxIndex

def znajdzZadanieKrytyczne(sigma, pierwszyIndexZadania, ostatniIndexZadania):
    #print("Pierwszy index zadania", pierwszyIndexZadania, " ostatni index=",ostatniIndexZadania)
    maxIndex=-100
    #print("dbg=pierwszyindex",pierwszyIndexZadania, "ostatniindex", ostatniIndexZadania, "len(sigma)", len(sigma))
    for i in range(pierwszyIndexZadania, ostatniIndexZadania+1):
        if(sigma[i].q<sigma[ostatniIndexZadania].q):
            maxIndex=i
    if(maxIndex==-100):
        return 0
    return maxIndex

N=l_zadania
UB=999999 #gorne oszacowanie wartosci funkcji celu - dla najlepszego dotychczas rozwiazania
LB=0 #dolne oszacowanie wartosci funkcji celu
PI_ST=[] #optymalna permutacja wykonania zadan na maszynie
PI=[] #permutacja wykonania zadan na maszynie
U=0 #wartosc funkcji celu
Kr = 99999
Kp = 0
Kq = 99999
Khr = 99999
Khp = 0
Khq = 99999
def Carlier(arg_l_zadania):
    #print("carlier")
    global carliercmax
    global tecmax
    global N
    global znalezionoOptymalneRozwiazanie
    global UB
    global LB
    global PI_ST
    global PI
    global U
    global Kr
    global Kp
    global Kq
    global Khr
    global Khp
    global Khq
    #N=arg_l_zadania.copy()
    #UB=0 #gorne oszacowanie wartosci funkcji celu - dla najlepszego dotychczas rozwiazania
    #LB=0 #dolne oszacowanie wartosci funkcji celu
    #PI_ST=[] #optymalna permutacja wykonania zadan na maszynie
    #PI=[] #permutacja wykonania zadan na maszynie
    #U=0 #wartosc funkcji celu

    #print("####GALAZ####")
    temp=Schrage(arg_l_zadania) #[0] - cmax    [1]-kolejnosc
    #print("$$wynik dzialania schrage",temp)
    PI=temp[1] #kolejnosc uzyskana z algorytmu Schrage
    U=temp[0] #cmax uzyskany z algorytmu Schrage
    #print("U=",U," UB=",UB)
    if(U<UB): #znaleziono lepsze rozwiazanie
        UB=U
        PI_ST=PI.copy() #najlepsze rozwiazanie do tej pory
        #print("znaleziono dobre rozw, kolejnosc", PI)

    #print("%$#kolejnosc",PI_ST)


    #wybor zadan
    b=znajdzOstatnieZadanieNaSciezceKrytycznej(PI) #indeks ostatniego zadania
    a=znajdzPierwszeZadanieNaSciezceKrytycznej(PI, b)
    c=znajdzZadanieKrytyczne(PI,a,b)
    #print("a=",a,"b=",b,"c=",c)
    if(c==0): #znaleziono optymalna kolejnosc
        #print("znaleziono optymalna kolejnosc!, nowa kolejnosc", PI_ST)
        optKol=PI_ST.copy()
        znalezionoOptymalneRozwiazanie=True
        return optKol

    #for i in range(c + 1, b + 1):

    #linia 13, szukamy czasow spelniajacych podane kryteria
    Kr=999999
    Kq=999999
    Kp=0
    for i in range (c+1,b+1):
        #print("~~~~ maxrange",b+1, "size", len(PI))
        Kr = min(Kr,PI[i].r)
        Kp += PI[i].p
        Kq = min(Kq,PI[i].q)
        #print("Znalezione kr=",Kr, " kp=",Kp, " Kq=", Kq)
    Kh = Kr + Kp + Kq
    Khp=0
    Khr=99999
    Khq=99999
    for j in range(c, b+1):
        Khr = min(Khr, PI[j].r)
        Khp += PI[j].p
        Khq = min(Khq, PI[j].q)
    Khc = Khr + Khp + Khq #h(K)
    StoreR = PI[c].r #zapamietaj r_pi(c)
    PI[c].r= max(PI[c].r, Kr + Kp)
    LB = Schrage_z_przerwaniami(PI)[0]
    LB = max(Kh,Khc,LB)
    #print("1: LB=", LB, "UB=", UB)
    if(LB < UB):
        Carlier(PI) #tworze nowy wezel ze zmodyfikowanym r
    PI[c].r = StoreR #odtworz r_pi(c)
    StoreQ=PI[c].q #zapamietaj q_pi(c)
    PI[c].q = max(PI[c].q, Kq + Kp)
    LB = Schrage_z_przerwaniami(PI)[0]
    LB = max(Kh, Khc, LB)
    #print("2: LB=",LB,"UB=",UB)
    if LB < UB:
        Carlier(PI) #tworze nowy wezel ze zmodyfikowanym q
    PI[c].q=StoreQ #odtworz q_pi(c)
    #tecmax =funkcjaCelu()



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

def Schrage_z_przerwaniami(arg_l_zadania):
    #inicjalizacja
    NN=[]
    NG=[]
    sigma=[]

    N=arg_l_zadania.copy()
    NN=N #zadania nieuszeregowane
    NG=[] # zadania gotowe
    t=0 #chwila czasowa #todo: poprawic z zera
    global cmax
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
print("SPDLab 5")
wczytajDaneZFolderu(nazwaKatalogu)
for nazwaPliku in l_nazwyPlikow:
    print("###########################################################")
    print("*nazwa przetwarzanego pliku", nazwaPliku)
    cmaxSchrage=0
    cmaxPrzerwania=0
    tempcmax = 0
    cmax = 0

    wczytajDaneZPlikuSCHRAGE("daneLab5/" + nazwaPliku)
    Schrage(l_zadania)
    #print("cmax Schrage=", tempcmax)
    wczytajDaneZPlikuSCHRAGE("daneLab5/" + nazwaPliku)
    Schrage_z_przerwaniami(l_zadania)
    #print('cmax Schrage z przerwaniami:', cmax)
    wczytajDaneZPlikuSCHRAGE("daneLab5/" + nazwaPliku)
    #print("####### CARLIER ##########################################")
    znalezionoOptymalneRozwiazanie=False
    Carlier(l_zadania)
    if znalezionoOptymalneRozwiazanie:
        uzyskanyCmax=funkcjaCelu(PI_ST)
        if prawidlowy_wynik==uzyskanyCmax:
            print("----PRAWIDLOWY WYNIK----")
        print("Carlier: prawidlowy cmax=", prawidlowy_wynik, "uzyskany cmax=", uzyskanyCmax)#, "optymalna kolejnosc=",PI_ST)
    else:
        print("Carlier: nie znaleziono optymalnego rozwiazania!")

    N = l_zadania
    UB = 999999  # gorne oszacowanie wartosci funkcji celu - dla najlepszego dotychczas rozwiazania
    LB = 0  # dolne oszacowanie wartosci funkcji celu
    PI_ST = []  # optymalna permutacja wykonania zadan na maszynie
    PI = []  # permutacja wykonania zadan na maszynie
    U = 0  # wartosc funkcji celu
    Kr = 99999
    Kp = 0
    Kq = 99999
    Khr = 99999
    Khp = 0
    Khq = 99999
    #print("cmax Carier=", cmax)1