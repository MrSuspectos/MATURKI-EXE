with open('trojki.txt','r') as file:
    trojki = []
    for line in file:
        a,b,c = map(int,line.split())
        trojki.append([a,b,c])

zgodne_z_zadaniem = []
for tro in trojki:
    suma = 0
    for x in str(tro[0]):
        suma += int(x)
    for x in str(tro[1]):
        suma += int(x)
    if suma == tro[2]:
        zgodne_z_zadaniem.append(tro)

print(zgodne_z_zadaniem)
print(len(zgodne_z_zadaniem))