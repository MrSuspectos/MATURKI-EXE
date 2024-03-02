with open('dane_napisy.txt') as f:
    pary_anagramow = []
    for line in f:
        a,b = map(str,line.strip().split(' '))
        pary_anagramow.append([a,b])

spelniajace = []
for para in pary_anagramow:
    dlugosc_a = len(para[0])
    dlugosc_b = len(para[1])
    if dlugosc_a != dlugosc_b: continue
    posortowana_a = sorted(para[0])
    posortowana_b = sorted(para[1])
    if posortowana_a == posortowana_b: spelniajace.append(para)

print('W pliku znajduje sie:',len(spelniajace),'par')