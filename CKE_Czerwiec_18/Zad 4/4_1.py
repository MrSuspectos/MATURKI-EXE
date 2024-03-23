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

n = len(dane1)
licznik = 0
for x in range(n):
    szybcior = len(dane1[x])-1
    if dane1[x][szybcior] == dane2[x][szybcior]: licznik += 1

print(licznik)