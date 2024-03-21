with open('instrukcje.txt','r') as f:
    dane = []
    for line in f:
        a,b = map(str, line.strip().split(" "))
        dane.append([a,b])

wyraz = []
for komenda in dane:
    if komenda[0] == "DOPISZ": wyraz.append(komenda[1])
    if komenda[0] == "ZMIEN":
        wyraz.pop()
        wyraz.append(komenda[1])
    if komenda[0] == "USUN": wyraz.pop()
    if komenda[0] == "PRZESUN":
        if wyraz.count(komenda[1]) > 0:
            przesunieta = ord(komenda[1]) + 1
            if przesunieta == 91: przesunieta = 65
            for i in range(len(wyraz)):
                if wyraz[i] == komenda[1]:
                    wyraz[i] = chr(przesunieta)
                    break
print(len(wyraz))