with open('punkty.txt','r') as f:
    dane = []
    for line in f:
        a,b = map(int, line.strip().split(' '))
        dane.append([a,b])

wewnatrz = 0
boki = 0
zewnatrz = 0
for punkt in dane:
    if punkt[0] < 5000 and punkt[0] > -5000 and punkt[1] < 5000 and punkt[1] > -5000:
        wewnatrz += 1
        continue
    if punkt[0] == 5000 or punkt[0] == -5000 or punkt[1]== -5000 or punkt[1] == 5000:
        if punkt[0] <= 5000 and punkt[0] >= -5000 and punkt[1] <= 5000 and punkt[1] >= -5000:
            boki += 1
            continue
    zewnatrz += 1


print('wewnątrz', wewnatrz)
print('boki', boki)
print('zewnątrz', zewnatrz)