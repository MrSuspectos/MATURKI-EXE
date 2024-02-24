wyraz = 'INFORMATYKA'
klucz = [3,2,5,4,1]

def szyfrowanie(wyraz,klucz):
    tablica_wyraz = []
    for a in wyraz:
        tablica_wyraz.append(a)
    for i in range(len(tablica_wyraz)):
        tablica_wyraz[i], tablica_wyraz[klucz[i % len(klucz)]-1] = tablica_wyraz[klucz[i % len(klucz)]-1], tablica_wyraz[i]
    return ''.join(tablica_wyraz)

print(szyfrowanie(wyraz,klucz))