with open('galerie.txt', 'r') as f: dane = [line.strip().split() for line in f]

odpowiedzi = []
for galeria in dane:
    miasto = galeria[1]
    licznik_lokali = set()
    for x in range(2, 140,2):
        temp_pow = int(galeria[x]) * int(galeria[x+1])
        if temp_pow == 0: continue
        licznik_lokali.add(temp_pow)
    odpowiedzi.append([len(licznik_lokali), miasto])

print(max(odpowiedzi), min(odpowiedzi))