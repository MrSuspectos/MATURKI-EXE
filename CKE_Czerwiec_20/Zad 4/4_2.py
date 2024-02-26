with open('pary.txt','r') as file:
    kochane_pary_brak_ich = []
    for x in file:
        a,b = map(str, x.split())
        kochane_pary_brak_ich.append(b)

tab = []
for line in kochane_pary_brak_ich:
    litera = None
    licznik = 1
    naj_ciag = 0
    for char in range(len(line)-1):
        if line[char] == line[char-1]:
            licznik += 1
            if licznik > naj_ciag:
                naj_ciag = licznik
                litera = line[char]
                continue
            continue
        licznik = 1
    if naj_ciag == 0:
        tab.append([line[0],1])
        continue
    tab.append([litera,naj_ciag])

for i in tab:
    print(''.join([i[0] for x in range(int(i[1]))]), i[1])