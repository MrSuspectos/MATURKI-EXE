obrazki = []
with open('dane_obrazki.txt', 'r') as file:
    obraz = []
    for line in file:
        line = line.strip()
        if line:  # jeśli linia nie jest pusta
            obraz.append(line)
        else:  # jeśli linia jest pusta, dodaj obrazek i zacznij nowy
            obrazki.append(obraz)
            obraz = []
    if obraz:  # jeśli plik nie kończy się pustą linią, dodaj ostatni obrazek
        obrazki.append(obraz)

licznik_rewersów = 0
naj_czarnych_pikseli = 0
for x in obrazki:
    piksele_czarne = 0
    for y in range(20):
        wiersz = x[y]
        piksele_czarne += wiersz[:-1].count('1')
    if piksele_czarne > 200:
        licznik_rewersów += 1
        if piksele_czarne > naj_czarnych_pikseli:
            naj_czarnych_pikseli = piksele_czarne

print('Liczba rewersów: ',licznik_rewersów)
print('Najciemniejszy obrazek: ',naj_czarnych_pikseli)