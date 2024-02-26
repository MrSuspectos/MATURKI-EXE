def jaka_pierwsza(x):
    tab = []
    for i in range(1,x+1):
        tabv2 = []
        if i < 2: continue
        for j in range(1,i+1):
            if i % j == 0:
                tabv2.append(j)
        if len(tabv2) == 2:
            tab.append(i)
    return tab


with open('pary.txt','r') as file:
    kochane_pary_brak_ich = []
    for x in file:
        a,b = map(str, x.split())
        kochane_pary_brak_ich.append(int(a))

dodatnie = []
tabv3 = []
for line in kochane_pary_brak_ich:
    if line % 2 == 0:
        tabv3.append(line)
        liczba = jaka_pierwsza(line)[-2]
        wynik = line - liczba
        dodatnie.append([wynik,liczba])


for x in range(len(tabv3)):
    print(f'{tabv3[x]}, {dodatnie[x]}')