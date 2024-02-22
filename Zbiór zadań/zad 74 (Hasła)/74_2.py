with open('hasla.txt','r') as file: hasla = [line.strip() for line in file]

hasla2 = []
licznik = 0
odp = []
for x in hasla:
    hasla2.append(x)
    if hasla2.count(x) == 2: odp.append(x)

posortowane = sorted(odp)
for x in posortowane: print(x)