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

#mhm dokładnie tutaj kończy się mój pomysł na to zadanie