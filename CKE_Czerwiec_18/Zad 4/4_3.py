def te_same_liczby(tablica):
    mhm = set()
    for i in tablica:
        mhm.add(i)
    return mhm

with open('dane1.txt','r') as f:
    dane1 = []
    for line in f:
        tym = line.strip()
        dane1.append(tym.split(" "))
with open('dane2.txt','r') as f:
    dane2 = []
    for line in f:
        tym = line.strip()
        dane2.append(tym.split(" "))

licznik = 0
odp = []
for x in range(len(dane2)):
    if te_same_liczby(dane2[x]) == te_same_liczby(dane1[x]):
        licznik += 1
        odp.append(x+1)

print('Takie same wiersze:',licznik,'Wystepija w (wierszach)', odp)