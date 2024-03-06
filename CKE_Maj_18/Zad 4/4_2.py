def rozne_liczby(n):
    licznik = set()
    for i in n: licznik.add(i)
    return len(licznik)

with open('sygnaly.txt','r') as f: sygnaly = [line.strip() for line in f]

spelniajace = []
naj = 0
for pojedynczy in sygnaly:
    liczba = rozne_liczby(pojedynczy)
    if liczba == naj: spelniajace.append(pojedynczy)
    if liczba > naj:
        spelniajace.clear()
        naj = liczba
        spelniajace.append(pojedynczy)

print(naj, spelniajace[0])