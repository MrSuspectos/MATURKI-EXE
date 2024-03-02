with open('dane_napisy.txt') as f:
    pary_anagramow = []
    for line in f:
        a,b = map(str,line.strip().split(' '))
        pary_anagramow.append([a,b])

spelniajace = []
for para in pary_anagramow:
    dlugosc_a = len(para[0])
    dlugosc_b = len(para[1])
    zgodnosc = True
    if dlugosc_a != dlugosc_b: continue
    for x in range(dlugosc_a):
        if para[0][x] != para[1][x]: zgodnosc = False
    if zgodnosc: spelniajace.append(para)

print('W pliku znajduje sie:',len(spelniajace),'par')