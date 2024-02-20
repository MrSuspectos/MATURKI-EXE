file = open('liczby2.txt','r')

liczby = ""
liczby2 = ""
liczba6osemkowo = 0
liczba6dziesiestnie = 0
for line in file:
    line.strip()
    liczby += line
    liczby2 += oct(int(line))

for i in liczby:
    liczba6dziesiestnie += str(i).count('6')
for i in liczby2:
    liczba6osemkowo += str(i).count('6')

print('Liczby dziesietne:',liczba6dziesiestnie)
print('Liczby osemkowo:',liczba6osemkowo)