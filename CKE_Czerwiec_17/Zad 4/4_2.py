def cyfropodobne(n):
    tablica = set()
    for i in n:
        tablica.add(i)
    return tablica

with open('punkty.txt', 'r') as f:
    dane = [line.strip().split(' ') for line in f]

odpowiedzi = 0
for liczby in dane:
    if cyfropodobne(liczby[0]) == cyfropodobne(liczby[1]): odpowiedzi += 1

print(odpowiedzi)