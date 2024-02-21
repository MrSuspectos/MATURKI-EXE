def pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(liczba**0.5) + 1):
        if liczba % i == 0:
            return False
    return True

def czy_polpierwsza(liczba):
    if liczba < 4:
        return False
    for i in range(2, liczba):
        if pierwsza(i) and liczba % i == 0:
            pierwsza_czesc = i
            druga_czesc = liczba // i
            if pierwsza(pierwsza_czesc) and pierwsza(druga_czesc):
                return True
    return False

polpierwsze = []
with open('ciagi.txt', 'r') as file:
    ciag = [line.strip() for line in file]

for binarka in ciag:
    liczba_d = int(binarka, 2)
    if czy_polpierwsza(liczba_d):
        polpierwsze.append(liczba_d)

print(f"Ilość ciągów reprezentujących liczby półpierwsze: {len(polpierwsze)} Największa liczba półpierwsza: {max(polpierwsze)} Najmniejsza liczba półpierwsza: {min(polpierwsze)}")