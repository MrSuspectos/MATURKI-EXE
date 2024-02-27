import math

with open('liczby.txt', 'r') as f: liczby = [int(line.strip()) for line in f]

wz_pierwsze = []
for pier in liczby:
    warunek = True
    for druga in liczby:
        if math.gcd(druga, pier) != 1:
            if pier == druga: continue
            warunek = False
            break
    if warunek: wz_pierwsze.append(pier)
print(max(wz_pierwsze))