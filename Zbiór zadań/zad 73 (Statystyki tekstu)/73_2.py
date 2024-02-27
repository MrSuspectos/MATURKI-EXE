# Co zlego to nie ja XDD

from collections import Counter
import string


def statystyka_czestotliwosci(tekst):
    # Usuwanie spacji
    tekst_bez_spacji = tekst.replace(" ", "")
    # Obliczanie częstotliwości występowania liter
    czestosci = Counter(tekst_bez_spacji)
    # Suma wystąpień liter
    suma_wystapien = sum(czestosci.values())

    statystyka = {}
    for litera in string.ascii_uppercase:  # Użyj wszystkich liter alfabetu
        liczba_wystapien = czestosci.get(litera, 0)  # Jeśli litera nie występuje, zwróć 0
        # Obliczanie procentowego udziału
        procentowy_udzial = (liczba_wystapien / suma_wystapien) * 100
        # Zaokrąglenie do dwóch miejsc po przecinku
        procentowy_udzial = round(procentowy_udzial, 2)
        statystyka[litera] = f"{liczba_wystapien} ({procentowy_udzial}%)"

    return statystyka


# Wczytanie tekstu z pliku
with open("tekst.txt", "r") as file:
    tekst = file.read()

wyniki = statystyka_czestotliwosci(tekst)
for litera, statystyka in sorted(wyniki.items()):
    print(f"{litera}: {statystyka}")