with open('instrukcje.txt','r') as f:
    dane = []
    for line in f:
        a,b = map(str, line.strip().split(" "))
        dane.append(a)

naj = ['',0]
licznik = 1
for x in range(len(dane)-1):
    if dane[x] == dane[x + 1]:
        licznik += 1
        if licznik > naj[1]:
            naj[1] = licznik
            naj[0] = dane[x]
    if dane[x] != dane[x + 1]: licznik = 1
print(naj)