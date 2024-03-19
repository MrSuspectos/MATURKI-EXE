with open('anagram.txt','r') as f: dane = [line.strip() for line in f]

podpunkt_a = 0
podpunkt_b = 0
suma = 0
for anagram in dane:
    dzies = int(anagram,2)
    if str(dzies).count('0') == 0: podpunkt_a += 1
    cos = set()
    for x in str(dzies): cos.add(x)
    prowizorka_wynik = 0
    for x in cos:
        prowizorka_wynik += int(x)
    if prowizorka_wynik > suma:
        podpunkt_b = dzies
        suma = prowizorka_wynik

print(podpunkt_a)
print(podpunkt_b)