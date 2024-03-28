def waga_liczby(n):
    while len(str(n)) != 1:
        waga = 0
        for i in n:
            waga += int(i)
        n = str(waga)
    return int(n)

with open('pierwsze.txt','r') as f: dane = [line.strip() for line in f]

for liczba in dane:
    if waga_liczby(liczba) == 1: print(liczba)