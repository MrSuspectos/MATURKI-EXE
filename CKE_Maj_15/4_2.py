with open('liczby.txt', 'r') as f: dane = [line.strip() for line in f]

podzielne_2 = 0
podzielne_8 = 0
for liczba in dane:
    liczba_dziesietnie = int(liczba,2)
    if liczba_dziesietnie % 2 == 0: podzielne_2 += 1
    if liczba_dziesietnie % 8 == 0: podzielne_8 += 1

print('Podzielne przez 2: ',podzielne_2)
print('Podzielne przez 8: ',podzielne_8)