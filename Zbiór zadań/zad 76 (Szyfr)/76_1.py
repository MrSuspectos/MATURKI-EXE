with open('szyfr1.txt','r') as file:
    odczytane = file.readlines()
    dozaszyfrowania = [line.strip() for line in odczytane[:6]]
    klucz = [int(x) for x in odczytane[6].split()]

def szyfrowanie(wyraz,klucz):
    tablica_wyraz = []
    for a in wyraz:
        tablica_wyraz.append(a)
    for i in range(len(tablica_wyraz)):
        #To działa w taki sposób że zamienia wartości w sposób w uproszeniu nie można tego zapisać w takich dwóch działaniach.
        # tablica_wyraz[i] = tablica_wyraz[klucz[i % len(klucz)]-1]
        # tablica_wyraz[klucz[i % len(klucz)]-1] = tablica_wyraz[i]
        tablica_wyraz[i], tablica_wyraz[klucz[i % len(klucz)]-1] = tablica_wyraz[klucz[i % len(klucz)]-1], tablica_wyraz[i]
    return ''.join(tablica_wyraz)

for x in dozaszyfrowania:
    print(szyfrowanie(x,klucz))

