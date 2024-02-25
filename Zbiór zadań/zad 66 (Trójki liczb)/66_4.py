with open('trojki.txt','r') as file:
    trojki = []
    for line in file:
        a,b,c = map(int, line.split())
        trojki.append(sorted([a,b,c]))

max_ciag = 0
ciag = 0
licznik = 0
for i in range(len(trojki)):
    if trojki[i][0] + trojki[i][1] > trojki[i][2]:
        licznik += 1
        ciag += 1
        continue
    if ciag > max_ciag: max_ciag = ciag
    else: ciag = 0


print('Wiersze w kótrych liczby reprezentują długości boków trójkąta:', licznik)
print('Najdłuższy ciąg trójkątnego:', max_ciag)