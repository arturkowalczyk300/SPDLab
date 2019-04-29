print("Lab 4 - Schrage")
import os
import random
import math
import time
print("SPD Lab 03")


nazwaKatalogu = "daneLab4"  # od teraz bedzie wczytywac wszystkie instancje z katalogu
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

print("SPDLab 3")
wczytajDaneZFolderu(nazwaKatalogu)

for nazwaPliku in l_nazwyPlikow:
    print("*nazwa przetwarzanego pliku", nazwaPliku)
    wczytajDaneZPliku("daneLab4/" + nazwaPliku)
print("gotowe")