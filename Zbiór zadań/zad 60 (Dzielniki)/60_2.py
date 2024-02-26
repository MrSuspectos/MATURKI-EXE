def czy_liczba_ma_18_dzielnikow(liczba):
    liczba = int(liczba)
    tablica = []
    for i in range(1, liczba+1):
        if liczba % i == 0:
            tablica.append(i)
    if len(tablica) == 18:
        return tablica
    else: return 0

with open('liczby.txt', 'r') as f: liczby = [line.strip() for line in f]

odp = []
for x in liczby:
    liczba = czy_liczba_ma_18_dzielnikow(x)
    if liczba != 0:
        odp.append([x, liczba])

for x in odp: print(x)