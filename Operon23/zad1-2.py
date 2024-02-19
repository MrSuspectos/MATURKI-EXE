def czy_liczba_jest_pierwsza(x):
    if x < 2:
        return False
    dzielniki = []
    for i in range(1,x+1):
        if x % i == 0:
            dzielniki.append(i)
    if len(dzielniki) == 2:
        return True
    else:
        return False

pliczek = open('przedzialy.txt', 'r')

liczby_pierwsze = []
licznik = 1
naj_liczb_pierwszych = 0
for line in pliczek:
    line = line.strip()
    lewy = line[0]
    prawy = line[-1]
    a = int(line.split(lewy)[1].split(',')[0])
    b = int(line.split(prawy)[0].split(',')[1])

    liczby = []
    for i in range(a, b):
        liczby.append(i)

    if lewy == '(':
        liczby.pop(0)
    if prawy == '>':
        liczby.append(b)

    liczby_ktore_sa_pierwsze = 0
    for j in liczby:
        if czy_liczba_jest_pierwsza(j):
            liczby_ktore_sa_pierwsze += 1

    if naj_liczb_pierwszych < liczby_ktore_sa_pierwsze:
        liczby_pierwsze.clear()
        liczby_pierwsze.append(line)
        naj_liczb_pierwszych = liczby_ktore_sa_pierwsze
    elif naj_liczb_pierwszych == liczby_ktore_sa_pierwsze:
        liczby_pierwsze.append(line)

    licznik += 1

print('Największe przedziały: ',liczby_pierwsze)