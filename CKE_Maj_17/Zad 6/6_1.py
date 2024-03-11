with open('dane.txt', 'r') as f: linie = [line.strip().split(' ') for line in f]

min = 999
max = 0
for i in linie:
    for j in i:
        if int(j) < min: min = int(j)
        if int(j) > max: max = int(j)

print('Najciemniejszy',min,'\nNajjaśniejszy',max)