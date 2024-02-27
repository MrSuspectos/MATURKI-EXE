with open('tekst.txt','r') as file:
    slowa = []
    for x in file:
        slowa.append(x.split(' '))

licznik = 0
for i in slowa:
    for j in i:
        dlugosc_j = len(j)
        if dlugosc_j == 1:
            continue
        for z in range(dlugosc_j-1):
            if j[z] == j[z+1]:
                licznik += 1
                break
print(licznik)
