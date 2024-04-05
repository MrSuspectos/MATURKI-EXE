import math

with open('punkty.txt','r') as f:
    dane = []
    for line in f:
        a,b = map(int, line.strip().split(' '))
        dane.append([a,b])

odpowiedz = [0]
for punktA in dane:
    for punktB in dane:
        odleglosc = round(math.sqrt(((punktB[0]-punktA[0])**2) + ((punktB[1]-punktA[1])**2)),0)
        if odleglosc > odpowiedz[0]:
            odpowiedz.clear()
            odpowiedz.append(int(odleglosc))
            odpowiedz.append([punktA,punktB])

print(odpowiedz)
