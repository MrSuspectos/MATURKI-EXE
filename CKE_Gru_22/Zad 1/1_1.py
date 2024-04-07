with open('mecz.txt','r') as f: dane = [line.strip() for line in f.readline()]

odp = 0
for mecz in range(0,9999):
    if dane[mecz] != dane[mecz+1]: odp += 1

print(odp)