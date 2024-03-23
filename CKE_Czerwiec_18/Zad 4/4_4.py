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
odp = []
for i in range(n):
    temp = []
    for j in range(len(dane1[i])):
        temp.append(int(dane1[i][j]))
        temp.append(int(dane2[i][j]))
    odp.append(sorted(temp))

for x in odp:
    for y in x: print(y,end=' ')
    print()