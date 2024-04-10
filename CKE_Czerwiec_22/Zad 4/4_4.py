with open('liczby.txt','r') as f:
    dane = []
    sprawdzenie = set()
    for line in f:
        dane.append(line.strip())
        sprawdzenie.add(line.strip())

dwa_razy = 0
trzy_razy = 0

for liczba in sprawdzenie:
    if dane.count(liczba) == 2: dwa_razy += 1
    if dane.count(liczba) == 3: trzy_razy += 1

print(len(sprawdzenie), dwa_razy, trzy_razy)