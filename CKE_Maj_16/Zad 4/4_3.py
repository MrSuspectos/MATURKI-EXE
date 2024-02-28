import math

with open('punkty.txt', 'r') as f:
    punkciki = []
    for line in f:
        x,y = map(float, line.split())
        punkciki.append([x,y])

poke_kwadratu = 400*400
zgodne_punkty = []
sierodek_kola = [200,200]
for punkty in punkciki[:1000]:
    wynik = ((punkty[0] - sierodek_kola[0]) ** 2) + ((punkty[1] - sierodek_kola[1]) ** 2)
    if wynik <= 200**2:
        zgodne_punkty.append(punkty)

pi_1000 = (poke_kwadratu * len(zgodne_punkty)) / (1000 * 200**2)

zgodne_punkty.clear()
for punkty in punkciki[:1700]:
    wynik = ((punkty[0] - sierodek_kola[0]) ** 2) + ((punkty[1] - sierodek_kola[1]) ** 2)
    if wynik <= 200**2:
        zgodne_punkty.append(punkty)
pi_1700 = (poke_kwadratu * len(zgodne_punkty)) / (1700 * 200**2)

e_1000 = (math.pi - pi_1000).__abs__()
e_1700 = (math.pi - pi_1700).__abs__()
print(e_1000, e_1700)