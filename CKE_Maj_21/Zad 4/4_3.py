with open('instrukcje.txt','r') as f:
    dane = []
    for line in f:
        a,b = map(str, line.strip().split(" "))
        dane.append([a,b])

najczestsza = []
licznik = 0
for komenda in dane:
    if komenda[0] == "DOPISZ":
        temp = dane.count(komenda)
        if temp > licznik:
            licznik = temp
            najczestsza = komenda

print(licznik, najczestsza)