with open('dane.txt', 'r') as f: obrazke = [line.strip().split(" ") for line in f]

pionowy_kolor = 0
for i in range(320):
    prowizorka = 1
    for j in range(199):
        if obrazke[j][i] == obrazke[j+1][i]:
            prowizorka += 1
            if prowizorka > pionowy_kolor:
                pionowy_kolor = prowizorka
            continue
        prowizorka = 0

print(pionowy_kolor)

#Jak działa to git tak ????