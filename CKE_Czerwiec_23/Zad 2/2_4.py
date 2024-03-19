def bombelkowe(tablica):
    n = len(tablica)
    for i in range(n):
        for j in range(0, n-i-1):
            if tablica[j] > tablica[j+1]:
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
    return tablica

def sufiksy(n,s):
    slowo = [line.strip() for line in s]
    temp = []
    for x in range(int(n)):
        temp.append("".join(slowo))
        slowo = slowo[1:]
    # Bardzo proste sortowanie nie wiem czy nie jest zabronione
    # temp = sorted(temp)
    posortowane = bombelkowe(temp)
    return posortowane[0]

with open('slowa4.txt','r') as f: dane = [line.strip().split(' ') for line in f]

for linia in dane:
    print(sufiksy(linia[0],linia[1]))