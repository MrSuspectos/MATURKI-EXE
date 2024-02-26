def dzielniki(liczba):
    liczba = int(liczba)
    tab = []
    for i in range(1,liczba+1):
        if liczba % i == 0:
            tab.append(i)
    return tab

with open('liczby.txt', 'r') as f: liczby = [line.strip() for line in f]

odp = []
for liczba in liczby:
    dzk_liczby = dzielniki(int(liczba))
    for x in dzk_liczby:
        odp.append(x)

najwieksza = 0
policzone = 1000
odp = sorted(odp)
for x in range(1,policzone+1):
    licznik = odp.count(x)
    print(licznik)
    if licznik < policzone and licznik != 0:
        policzone = licznik
        print(x)
        najwieksza = x