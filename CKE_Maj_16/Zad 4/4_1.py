with open('punkty.txt', 'r') as f:
    punkciki = []
    for line in f:
        a,b = map(int, line.split())
        punkciki.append([a,b])

zgodne_punkty = []
sierodek_kola = [200,200]
licznik = 0
for punkty in punkciki:
    wynik = ((punkty[0] - sierodek_kola[0]) ** 2) + ((punkty[1] - sierodek_kola[1]) ** 2)
    if wynik == 200**2:
        zgodne_punkty.append(punkty)
    if wynik < 200**2:
        licznik += 1
print(zgodne_punkty)
print(licznik)