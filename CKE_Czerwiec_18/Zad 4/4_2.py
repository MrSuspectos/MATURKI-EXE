def sprawdzenie(tablica):
    p = 0
    n = 0
    for i in tablica:
        if int(i) % 2 == 0: p += 1
        if int(i) % 2 != 0: n += 1
    return True if p == n else False

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
for x in range(len(dane2)):
    if sprawdzenie(dane2[x]) and sprawdzenie(dane1[x]): licznik += 1

print(licznik)