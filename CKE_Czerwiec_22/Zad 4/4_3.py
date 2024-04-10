def liczba_pierwsza(n):
    licznik = 0
    for i in range(1,n+1):
        if n % i == 0: licznik += 1
    return True if licznik == 2 else False

with open('liczby.txt', 'r') as f: dane = [line.strip() for line in f]

for liczba in dane:
    odbicie = liczba[::-1]
    if liczba_pierwsza(int(odbicie)) and liczba_pierwsza(int(liczba)): print(liczba)