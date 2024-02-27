with open('tekst.txt', 'r') as file:
    slowa = []
    for x in file:
        slowa.extend(x.split())

spolgloski = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']

naj_slowo = 0
naj_ciag = 0
tablica_naj_slow = []
for wyraz in slowa:
    licznik = 0
    dlugosc_slowa = len(wyraz)
    for i in range(0, dlugosc_slowa):
        if wyraz[i].upper() in spolgloski:
            licznik += 1
        else:
            if licznik > naj_ciag:
                tablica_naj_slow.clear()
                naj_slowo = dlugosc_slowa
                naj_ciag = licznik
                tablica_naj_slow.append(wyraz)
            elif licznik == naj_ciag:
                tablica_naj_slow.append(wyraz)
            licznik = 0

print("Pierwsze takie wystapienie:", tablica_naj_slow[0])
print("Njadluzszy ciag spolglosek:", naj_ciag)
print("Znalezionych slowek:",len(tablica_naj_slow))
