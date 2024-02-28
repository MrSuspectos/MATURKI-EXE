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
print(round(pi_1000,4))

zgodne_punkty.clear()
for punkty in punkciki[:5000]:
    wynik = ((punkty[0] - sierodek_kola[0]) ** 2) + ((punkty[1] - sierodek_kola[1]) ** 2)
    if wynik <= 200**2:
        zgodne_punkty.append(punkty)
pi_5000 = (poke_kwadratu * len(zgodne_punkty)) / (5000 * 200**2)
print(round(pi_5000,4))

zgodne_punkty.clear()
for punkty in punkciki:
    wynik = ((punkty[0] - sierodek_kola[0]) ** 2) + ((punkty[1] - sierodek_kola[1]) ** 2)
    if wynik <= 200**2:
        zgodne_punkty.append(punkty)
pi_wszystkie = (poke_kwadratu * len(zgodne_punkty)) / (10000 * 200**2)
print(round(pi_wszystkie,4))