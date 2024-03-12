def zwracanie_zakodowan_rozkodowany(tekst1, tekst2):
    rozkodowany = []
    zadkodowany = []
    for x in range(len(tekst1)):
        rozkodowany.append(ord(tekst1[x])-97)
        zadkodowany.append(ord(tekst2[x])-97)
    odpowiedz = []
    for x in range(26):
        for y in range(26):
            zminena = True
            for i in range(len(rozkodowany)):
                liczba = rozkodowany[i] * x + y
                if liczba % 26 != zadkodowany[i]:
                    zminena = False
                    break
            if zminena: odpowiedz.append([x, y])
    return odpowiedz

with open('probka.txt', 'r') as f: tekst = [line.strip().split(' ') for line in f]

for linia in tekst:
    klucze = zwracanie_zakodowan_rozkodowany(linia[0], linia[1])
    print(f"Słowo '{linia[0]}' zostało zaszyfrowane przez:")
    for klucz in klucze: print(f"A = {klucz[0]}, B = {klucz[1]}")
    print("Może być odszyfrowane przez:")
    for klucz in klucze:
        # Obliczenie klucza deszyfrującego (powalone jeśli mam być szczery)
        A_decrypt = pow(klucz[0], -1, 26)
        B_decrypt = (-A_decrypt * klucz[1]) % 26
        print(f"A = {A_decrypt}, B = {B_decrypt}")
