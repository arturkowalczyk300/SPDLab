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



N=l_zadania



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

# glowna czesc
print("SPDLab 5")
wczytajDaneZFolderu(nazwaKatalogu)
for nazwaPliku in l_nazwyPlikow:
    print("###########################################################")
    print("*nazwa przetwarzanego pliku", nazwaPliku)
