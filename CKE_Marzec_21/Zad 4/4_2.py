with open('galerie.txt', 'r') as f: dane = [line.strip().split() for line in f]

odpowiedzi = []
podpunkt_b = []
for galeria in dane:
    miasto = galeria[1]
    licznik_lokali = 0
    pow_galeri = 0
    for x in range(2, 140,2):
        if galeria[x] != '0': licznik_lokali += 1
        temp_pow = int(galeria[x]) * int(galeria[x+1])
        pow_galeri += temp_pow
    odpowiedzi.append([miasto, pow_galeri,licznik_lokali])
    podpunkt_b.append([pow_galeri, miasto])

for x in odpowiedzi:
    print(x[0],x[1],x[2])

print(max(podpunkt_b), min(podpunkt_b))