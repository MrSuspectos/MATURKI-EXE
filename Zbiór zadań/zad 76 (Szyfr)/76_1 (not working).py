with open('szyfr1.txt','r') as file:
    odczytane = file.readlines()
    dozaszyfrowania = [line.strip() for line in odczytane[:6]]
    klucz = [int(x) for x in odczytane[6].split()]

zaszyfrowany_tekst =[]
d_klucza = len(klucz)
for i in dozaszyfrowania:
    processzyforwania = ""
    for x in range(len(i)):
        index = (x % d_klucza)
        processzyforwania += i[x]
        processzyforwania = processzyforwania[:x] + i[klucz[index]-1] + processzyforwania[x+1:]
    zaszyfrowany_tekst.append(processzyforwania)

for x in zaszyfrowany_tekst: print(x)