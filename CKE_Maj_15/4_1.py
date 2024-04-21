with open('liczby.txt','r') as f: dane = [line.strip() for line in f]

odp = 0
for liczba in dane:
    zera = liczba.count('0')
    jedynki = liczba.count('1')
    if zera > jedynki: odp += 1

print(odp)