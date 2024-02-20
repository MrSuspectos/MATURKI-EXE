file = open('liczby1.txt','r')
file2 = open('liczby2.txt','r')

liczby = []
liczby2 = []
for line in file:
    line.strip()
    liczby.append(int(line, 8))
for line2 in file2:
    line2.strip()
    liczby2.append(line2)

takiesame = 0
liczby1_sa_wieksze = 0
for x in range(1000):
    if int(liczby[x]) == int(liczby2[x]):
        takiesame += 1
    elif int(liczby[x]) > int(liczby2[x]):
        liczby1_sa_wieksze += 1

print('Liczby takie same:', takiesame)
print('Liczby1 są większe:', liczby1_sa_wieksze)