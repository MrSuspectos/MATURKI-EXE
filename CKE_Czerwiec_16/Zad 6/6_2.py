with open('liczby.txt','r') as f: dane = [line.strip() for line in f]

czworkowe_bez_0 = 0
for liczba in dane:
    if liczba[-1] == '4':
        zmienna = True
        for x in range(len(liczba)-1):
            if liczba[x] == '0': zmienna = False
        if zmienna: czworkowe_bez_0 += 1
print(czworkowe_bez_0)