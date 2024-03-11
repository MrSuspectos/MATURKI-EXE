with open('dane.txt', 'r') as f: obrazke = [line.strip().split(" ") for line in f]

# Nigdy bym chyba na takie cos nie wpadł XF
zgodne_z_zadania = 0
kordy = ((1,0),(-1,0),(0,1),(0,-1))
for x in range(0,320):
    for y in range(0,200):
        licznik = 0
        for k in kordy:
            if x + k[0] > 319 or x + k[0] < 0 or y + k[1] > 199 or y + k[1] < 0: continue
            else:
                if abs(int(obrazke[y][x]) - int(obrazke[y + k[1]][x + k[0]])) > 128:
                    licznik += 1
        if licznik != 0: zgodne_z_zadania += 1

print(zgodne_z_zadania)