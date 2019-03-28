# Lista krokow:
# 1. generuj rozwiazanie poczatkowe
# 2. wykonaj losowy ruch
# 3. przelicz cmax
# 4. czy cmax jest mniejsze od poprzedniego?
# tak:
#     czy temperatura jest wieksza od Tk?
#     tak: T=T*wsp, wroc do kroku 2
#     nie: STOP
# nie: losuj rnd
# czy rnd < P?
#     tak:
#         nie rob nic
#     nie:
#         cofnij ruch
#     czy temperatura jest wieksza od Tk?
#         tak: T=T*wsp, wroc do kroku 2
#         nie: STOP
#
print("SPD Lab 03")
#zmienne poczatkowe
T=0; #aktualna temperatura
Tk=0 #temperatura koncowa
wsp=0 #wspolczynnik wychladzania
rnd=0 #liczba losowa z przedzialu (0,1)
Fakt=0 #wartosc funkcji celu(cmax) dla aktualnej permutacji
Fpoprz=0 #wartosc funkcji celu dla poprzedniej permutacji
Fdelta=0 #roznica funkcji celu (poprzednia minus aktualna)
P=0 #prawdopodobienstwo niekorzystnego ruchu