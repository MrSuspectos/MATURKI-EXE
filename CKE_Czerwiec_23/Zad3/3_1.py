with open('anagram.txt','r') as f: dane = [line.strip() for line in f]

zrownazone = 0
prawie_zrownazone = 0
for anagram in dane:
    zera = anagram.count('0')
    jedynki = anagram.count('1')
    if zera == jedynki: zrownazone += 1
    if abs(zera-jedynki) == 1: prawie_zrownazone += 1
print(zrownazone)
print(prawie_zrownazone)