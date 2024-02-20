file = open('liczby2.txt','r')

liczby = []
for line in file:
    line = line.strip()
    liczby.append(int(line))

pierwszyelement = 0
maxdlugosc = 1
count = 1
for x in range(1,len(liczby)):
    if liczby[x] >= liczby[x-1]:
        count += 1
    else:
        if count > maxdlugosc:
            maxdlugosc = count
            start_index = x - maxdlugosc
        count = 1

if count > maxdlugosc:
    maxdlugosc = count
    start_index = len(liczby) - maxdlugosc

pierwszyelement = liczby[start_index]
print('Pierwszy element:',pierwszyelement,'\nDlugość danego ciągu to:', maxdlugosc)