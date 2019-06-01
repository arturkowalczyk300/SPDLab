import os
from ortools.linear_solver import pywraplp
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

def MILP(arg_l_zadania):
    mySolver=pywraplp.Solver("SimpleMipProgram", "CBC_MIXED_INTEGER_PROGRAMMING")

    #maksymalna wartość zmiennych liczona z duza przesada
    variablesMaxValue=0
    for zadanie in arg_l_zadania:
        variablesMaxValue+=zadanie.r+zadanie.p+zadanie.q

    #zmienne
    #alfy potrzebne do ustalenia kolejnosci:
    alfas = mySolver.MakeIntVarMatrix(#####)
    #czasy rozpoczyannaia poszczegolnych zadan
    mySolver.v

# glowna czesc
print("SPDLab 5")
wczytajDaneZFolderu(nazwaKatalogu)
for nazwaPliku in l_nazwyPlikow:
    print("###########################################################")
    print("*nazwa przetwarzanego pliku", nazwaPliku)



from ortools.linear_solver import pywraplp
from pathlib import Path
class RPQ() :
    def __init__ (self, r, p, q ) :
        self.R = r
        self.P = p
        self.Q = q
def Milp( jobs , instanceName ) :
    variablesMaxValue = 0
    for i in range (len(jobs)):
    variablesMaxValue += ( jobs[i].R+jobs[i].P+jobs[i].Q)
    solver = pywraplp.Solver('simple_mip_program',pywraplp . Solver .CBC_MIXED_INTEGER_PROGRAMMING)
    #variables :
    alfasMatrix = {} #attention ! dictionary ¡not list !
    for i in range (len(jobs)):
        for j in range (len(jobs)):
            alfasMatrix [i,j] = solver.IntVar(0,1," alfa "+str(i)+"_"+str(j))
    starts = []
    for i in range ( len ( jobs ) ) :
        starts.append(solver.IntVar(0,variablesMaxValue,"starts"+str(i)))
    cmax = solver . IntVar (0 , variablesMaxValue , "cmax" )

    # constraints :
    for i in range ( len ( jobs ) ) :
        solver.Add(starts[i]>=jobs[i].R)
        solver.Add(cmax>= starts [ i ] + jobs [ i ] . P+jobs [ i ] .Q)
    for i in range ( len ( jobs ) ) :
        for j in range ( i +1 ,len ( jobs ) ) :
            solver.Add( starts[i]+jobs[i].P<=starts[j]+ alfasMatrix [i,j]*variablesMaxValue )
            solver.Add( starts[j]+jobs[j].P<=starts[i]+ alfasMatrix [j,i]*variablesMaxValue )
            solver.Add( alfasMatrix [ i , j ] + alfasMatrix [ j , i ] == 1)
    # solver:
    solver.Minimize(cmax)
    status = solver.Solve()
    if(status is not pywraplp.Solver.OPTIMAL) :
        print ( "Not optimal ! " )
    print (instanceName , "Cmax: " , solver . Objective ( ) . Value ( ) )
    pi = [ ]
    for i in range ( len(starts) ) :
        pi.append(( i, starts[i].solution_value ( ) ) )
    pi . sort ( key=lambda x : x [ 1 ])
    print (pi)
def GetRPQsFromFile( pathToFile ) :
    fullTextFromFile = Path( pathToFile ) . read_text ()
    words = fullTextFromFile.replace ( "\n" , " " ) . s p l it ( " " )
    words_cleaned = list(filter(None, words ))
    numbers = list(map( int , words_cleaned ))
    numberOfJobs = numbers[ 0]
    numbers .pop(0)
    numbers .pop(0)
    jobs = [ ]
    for i in range (numberOfJobs ) :
        jobs . append(RPQ(numbers[ 0] ,numbers[ 1] ,numbers [ 2 ] ) )
        numbers .pop(0)
        numbers .pop(0)
        numbers .pop(0)
    return jobs
if __name__ == '__main__ ' :
    file_paths = [ "data000 . t xt " ]
    for i in range ( len ( file_paths) ) :
        jobs = GetRPQsFromFile(file_paths[i])
        Milp( jobs , file_paths[i])