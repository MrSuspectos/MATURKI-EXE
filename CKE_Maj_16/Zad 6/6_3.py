def dezintegracja_cke(wyraz, wyraz_zaszyfrowany):
    odszyfrowane = [ord(line) for line in wyraz]
    zaszyfrowany = [ord(line1) for line1 in wyraz_zaszyfrowany]
    wynik = zaszyfrowany[0] - odszyfrowane[0]

    for x in range(len(wyraz)):
        if (zaszyfrowany[x] - odszyfrowane[x]) > 0 and wynik < 0:
            sprawdzenie = (zaszyfrowany[x] - odszyfrowane[x]) - 26
            if sprawdzenie != wynik:
                return True
            continue
        if (zaszyfrowany[x] - odszyfrowane[x]) < 0 and wynik > 0:
            sprawdzenie = (zaszyfrowany[x] - odszyfrowane[x]) + 26
            if sprawdzenie != wynik:
                return True
            continue
        if (zaszyfrowany[x] - odszyfrowane[x]) != wynik:
            return True
    return False

with open('dane_6_3.txt', 'r') as f:
    do_sprawdzenia = []
    for line in f:
        a,b = map(str, line.strip().split(" "))
        do_sprawdzenia.append([a,b])

tablica_zwrotna = []
for i in do_sprawdzenia:
    if dezintegracja_cke(i[0],i[1]):
        tablica_zwrotna.append(i)
print(tablica_zwrotna)