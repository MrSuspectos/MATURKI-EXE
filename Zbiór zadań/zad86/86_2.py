def wczytaj_dane(nazwa_pliku):
    dane = {}
    with open(nazwa_pliku, 'r') as plik:
        for linia in plik:
            linia = linia.strip().split()
            okreg = linia[0]
            dane[okreg] = [int(glosy) for glosy in linia[1:]]
    return dane

# Funkcja do obliczenia procentowego poparcia komitetu w danym okręgu
def oblicz_poparcie(dane):
    poparcie = {}
    for okreg, glosy in dane.items():
        suma_glosow = sum(glosy)
        for i, liczba_glosow in enumerate(glosy):
            procent = (liczba_glosow / suma_glosow) * 100
            procent = round(procent, 2)
            if i not in poparcie:
                poparcie[i] = (okreg, procent)
            else:
                if procent > poparcie[i][1]:
                    poparcie[i] = (okreg, procent)
    return poparcie

# Wczytanie danych z pliku
dane = wczytaj_dane("dane_wybory.txt")

# Obliczenie procentowego poparcia dla każdego komitetu w poszczególnych okręgach
poparcie = oblicz_poparcie(dane)

for komitet, (okreg, procent) in poparcie.items():
    print(f"{komitet + 1}. Okrąg mateczny dla komitetu K{komitet + 1}: {okreg}, poparcie: {procent}%\n")