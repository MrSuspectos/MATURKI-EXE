with open('tekst.txt') as f: tekst = [line.strip().split(' ') for line in f]

d_d = []
for wiersz in tekst:
    for x in wiersz:
        if x[0] == 'd' and x[len(x)-1] == 'd': d_d.append(x)

print(len(d_d),d_d)