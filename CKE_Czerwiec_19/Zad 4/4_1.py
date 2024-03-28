def czy_pierwsza(n):
    dzielniki = 0
    for x in range(1, n+1):
        if n % x == 0: dzielniki += 1
    return True if dzielniki == 2 else False

with open('liczby.txt', 'r') as f: dane = [line.strip() for line in f]

odp = []
for liczba in dane:
    if int(liczba) < 100 or int(liczba) > 5000: continue
    if czy_pierwsza(int(liczba)): odp.append(int(liczba))

for x in odp: print(x)