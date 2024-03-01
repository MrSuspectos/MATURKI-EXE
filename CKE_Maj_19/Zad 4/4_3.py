#Sorki nie mam pojęcia jak zrobić to na 5 punktów 4 muszą wam wystarczyć


def najwiekszy_wspolny_dzielnik(a, b):
    while b:
        a, b = b, a % b
    return a

def nwd_zbioru(liczby):
    nwd = liczby[0]
    for liczba in liczby[1:]:
        nwd = najwiekszy_wspolny_dzielnik(nwd, liczba)
    return nwd

def znajdz_najdluzszy_ciag(plik):
    najdluzszy_ciag = []
    aktualny_ciag = []

    with open(plik, 'r') as f:
        for line in f:
            liczba = int(line.strip())
            if not aktualny_ciag or najwiekszy_wspolny_dzielnik(aktualny_ciag[0], liczba) > 1:
                aktualny_ciag.append(liczba)
            else:
                if len(aktualny_ciag) > len(najdluzszy_ciag):
                    najdluzszy_ciag = aktualny_ciag.copy()
                aktualny_ciag = [liczba]

    if len(aktualny_ciag) > len(najdluzszy_ciag):
        najdluzszy_ciag = aktualny_ciag

    pierwsza_liczba = najdluzszy_ciag[0]
    dlugosc_ciagu = len(najdluzszy_ciag)
    dzielnik = nwd_zbioru(najdluzszy_ciag)

    return pierwsza_liczba, dlugosc_ciagu, dzielnik

plik = "liczby.txt"
wynik = znajdz_najdluzszy_ciag(plik)
print("Wartość pierwszej liczby w najdłuższym ciągu:", wynik[0])
print("Długość ciągu:", wynik[1])
print("Największy wspólny dzielnik wszystkich liczb w ciągu:", wynik[2])