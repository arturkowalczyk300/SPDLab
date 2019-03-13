# Sterowanie procesami dyskretnymi, laboratorium 2, 2019
#Algorytm NEH

#krok 1: wyzancz w(j)

# inicjalizacja struktur danych dla 2 maszyn
dwie_zadania = [10000, 10000, 10000, 10000]
dwie_czas_na_maszynie_1 = [10, 20, 200, 1]
dwie_czas_na_maszynie_2 = [10, 18, 3, 3]
dwie_liczba_maszyn = 2
dwie_liczba_zadan = len(dwie_zadania)

# inicjalizacja struktur danych dla 3 maszyn
trzy_zadania = [1000, 1000, 1000, 1000]
trzy_czas_na_maszynie_1 = [1, 7, 6, 8]
trzy_czas_na_maszynie_2 = [6, 12, 3, 1]
trzy_czas_na_maszynie_3 = [4, 11, 2, 18]
trzy_liczba_maszyn = 3

# w(j) = suma czasow 3 maszyn
n = trzy_zadania  # zadania
czas1 = trzy_czas_na_maszynie_1.copy()
czas2 = trzy_czas_na_maszynie_2.copy()
czas3 = trzy_czas_na_maszynie_3.copy()
czas_wszystkich_zadan_3 = czas1.copy()
for i in range(0, len(czas1)):
    czas_wszystkich_zadan_3[i] = czas1[i] + czas2[i] + czas3[i]
# w(j) = suma czasow 2 maszyn
n = dwie_zadania
czas1 = dwie_czas_na_maszynie_1.copy()
czas2 = dwie_czas_na_maszynie_2.copy()
czas_wszystkich_zadan_2 = czas1.copy()
for i in range(0, len(czas1)):
    czas_wszystkich_zadan_2[i] = czas1[i] + czas2[i]
#sortowanie zadań majejąco po w(j) przy 2 maszynach
a = list(n)  # tworzenie listy do n zadan#
posortowana=[]
print(czas_wszystkich_zadan_2)
for k in range(0, len(n)):
    Max2 = max(czas_wszystkich_zadan_2)
    index2 = czas_wszystkich_zadan_2.index(Max2)
    posortowana.append(index2 + 1)
    czas_wszystkich_zadan_2[index2] = 0

print(posortowana)

#sortowanie zadań malejąco po w(j) przy 3 maszynach

n = trzy_zadania
czas1 = trzy_czas_na_maszynie_1.copy()
czas2 = trzy_czas_na_maszynie_2.copy()
czas3 = trzy_czas_na_maszynie_3.copy()
czas_wszystkich_zadan_3 = czas1.copy()
for i in range(0, len(czas1)):
    czas_wszystkich_zadan_3[i] = czas1[i] + czas2[i] + czas3[i]
#sortowanie zadań majejąco po w(j) przy 2 maszynach
a = list(n)  # tworzenie listy do n zadan#
posortowana=[]
print(czas_wszystkich_zadan_3)
for k in range(0, len(n)):
    Max3 = max(czas_wszystkich_zadan_3)
    index3 = czas_wszystkich_zadan_3.index(Max3)
    posortowana.append(index3 + 1)
    czas_wszystkich_zadan_3[index3] = 0

print(posortowana)
