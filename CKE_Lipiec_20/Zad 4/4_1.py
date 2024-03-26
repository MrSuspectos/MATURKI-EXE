with open('identyfikator.txt','r') as f: dane = [line.strip() for line in f]

naj = 0
odp = []
for identyfikator in dane:
    wynik = 0
    for x in identyfikator[3:]: wynik += int(x)
    if wynik == naj: odp.append(identyfikator)
    if wynik > naj:
        naj = wynik
        odp.clear()
        odp.append(identyfikator)

print(odp)