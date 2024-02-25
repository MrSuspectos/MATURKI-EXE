with open('szyfr3.txt','r') as file: dozaszyfrowania = [line.strip() for line in file]
klucz = [6, 2, 4, 1, 5, 3]

def szyfrowanie(wyraz,klucz):
    tablica_wyraz = []
    for a in wyraz:
        tablica_wyraz.append(a)
    # Zaczęcie od końca pozwoliło doszyfrować tablicę YEAH
    for i in range(len(tablica_wyraz)-1,-1,-1):
        tablica_wyraz[i], tablica_wyraz[klucz[i % len(klucz)]-1] =  tablica_wyraz[klucz[i % len(klucz)]-1], tablica_wyraz[i]
    return ''.join(tablica_wyraz)

for x in dozaszyfrowania:
    print(szyfrowanie(x,klucz))