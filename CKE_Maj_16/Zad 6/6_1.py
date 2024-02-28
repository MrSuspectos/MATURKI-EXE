def szyfrowanie(wyraz):
    k = 107 % 26
    zaszyfrowane = []
    for x in wyraz:
        litera = ord(x)
        zaszyfrowana = litera + k
        if zaszyfrowana > 90:
            zaszyfrowana = zaszyfrowana - 26
        zaszyfrowane.append(chr(zaszyfrowana))
    return ''.join(zaszyfrowane)

with open('dane_6_1.txt', 'r') as f: do_zaszyfrowania = [line.strip() for line in f]

juz_zaszyfrowane = []
for wyraz in do_zaszyfrowania:
    juz_zaszyfrowane.append(szyfrowanie(wyraz))

print(juz_zaszyfrowane)