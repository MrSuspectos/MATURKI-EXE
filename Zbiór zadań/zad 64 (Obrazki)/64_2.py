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

liczbik_rekurencyjnych = 0
pierwszy_obrazki = True
pierwszy_obrazkek = []
for x in obrazki:
    zmienna = True

    for y in range(10):
        if x[y] != x[y+10]:
            zmienna = False
    if zmienna:
        liczbik_rekurencyjnych += 1
        if pierwszy_obrazki:
            pierwszy_obrazkek.append(x)
            pierwszy_obrazki = False

print(liczbik_rekurencyjnych)

for x in pierwszy_obrazkek:
    for y in x:
        print(y)