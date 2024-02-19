pliczek = open('przedzialy.txt', 'r')

nieparzyste = []
licznik = 1
naj_nieparzyste = 0
for line in pliczek:
    line = line.strip()
    lewy = line[0]
    prawy = line[-1]
    a = int(line.split(lewy)[1].split(',')[0])
    b = int(line.split(prawy)[0].split(',')[1])

    liczby = []
    for i in range(a,b):
        liczby.append(i)

    if lewy == '(':
        liczby.pop(0)
    if prawy == '>':
        liczby.append(b)

    nieparzyste_liczby = 0
    for j in liczby:
        if j % 2 != 0:
            nieparzyste_liczby += 1
    if naj_nieparzyste < nieparzyste_liczby:
        nieparzyste.clear()
        nieparzyste.append(licznik)
        naj_nieparzyste = nieparzyste_liczby
    elif naj_nieparzyste == nieparzyste_liczby:
        nieparzyste.append(licznik)

    licznik += 1

print('Wiersze: ',nieparzyste)
print('Największa ilość nieparzystych: ',naj_nieparzyste)