def sprawdzenie_identyfikatora(liczba):
    kontrolna = int(liczba[3])
    suma = 0
    wagi = [7,3,1,0,7,3,1,7,3,7,3,1,7,3,1,7,3]
    for x in range(len(liczba)):
        if x < 3: suma += (ord(liczba[x])-55) * wagi[x]
        if x == 3: continue
        if x > 3: suma += int(liczba[x]) * wagi[x]
    return False if suma % 10 == kontrolna else True

with open('identyfikator.txt','r') as f: dane = [line.strip() for line in f]

niepoprawne = []
for identyfikator in dane:
    if sprawdzenie_identyfikatora(identyfikator): niepoprawne.append(identyfikator)

for x in niepoprawne: print(x)