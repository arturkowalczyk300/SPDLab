
"""
#algorytm Johnsona dla wariantu 2-maszynowego
n #zadania
czas1=[] #czas zadan na m1
czas2=[] #czas zadan na m2
m1[n,czas1]
m2[n,czas2]
a=list(1,n) # tworzenie listy do n zadan
l1=[]
l2=[]
najkrotsza=[]
for n in a
Min1 = min(czas1)
Min2 = min(czas2)
if Min1 < Min2
a.remove(m1[n,Min1])
l1.append(m1[n,Min1])
elif Min2 < Min1
a.remove(m2[n,Min2])
l2.insert(0,m2[n,Min2])
elif Min1=Min2
a.remove(m1[n,Min1])
l1.append(m1[n,Min1]) #mozna wybrac losowo
Jeśli obie opcje znajdują się na komputerze 1,
 wybierz najpierw tę z dłuższą operacją 2

Jeśli oba są na maszynie 2,
wybierz najpierw tę z dłuższą operacją 1.


najkrotsza = l1 + l2
print(najkrotsza)



#Algorytm dla 3 maszyn
n #zadania
czas1=[] #czas zadan na m1
czas2=[] #czas zadan na m2
czas3=[] #czas zadan na m3
m1[n,czas1]
m2[n,czas2]
m2[n,czas3]
czasw1=[(czas1+czas2)]
czasw2=[(czas3+czas2)]
mw1=[n, czasw1] #wirtualna maszyna 1
mw2=[n, czasw2] #wirtualna maszyna 2
a=list(1,n) # tworzenie listy do n zadan
l1=[]
l2=[]
najkrotsza=[]
for n in a
Min1 = min(czasw1)
Min2 = min(czaw2)
if Min1 < Min2
a.remove(m1[n,Min1])
l1.append(m1[n,Min1])
elif Min2 < Min1
a.remove(m2[n,Min2])
l2.insert(0,m2[n,Min2])
elif Min1=Min2
a.remove(m1[n,Min1])
l1.append(m1[n,Min1]) #mozna wybrac losowo
Jeśli obie opcje znajdują się na komputerze 1,
 wybierz najpierw tę z dłuższą operacją 2

Jeśli oba są na maszynie 2,
wybierz najpierw tę z dłuższą operacją 1.


najkrotsza = l1 + l2
print(najkrotsza)
"""