def deszyfrowanie(wyraz, k_podane):
    k = int(k_podane) % 26
    odszyfrowane = []
    for x in wyraz:
        litera = ord(x)
        odszyfrowana = litera - k
        if odszyfrowana < 65:
            odszyfrowana = odszyfrowana + 26
        odszyfrowane.append(chr(odszyfrowana))
    return ''.join(odszyfrowane)

with open('dane_6_2.txt', 'r') as f:
    do_odszyfrowania = []
    for line in f:
        a,b = map(str, line.split(" "))
        do_odszyfrowania.append([a,b])


juz_odszyforwane = []
for wyraz in do_odszyfrowania[:700]:
    juz_odszyforwane.append(deszyfrowanie(wyraz[0],wyraz[1]))

print(juz_odszyforwane)