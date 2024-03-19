#       UWAGA NIE JEST TO DOKOŃCZONE NIE MAM INNEGO POMYSŁU JAK TO DOKOŃCZYĆ



def bombelkowe(tablica):
    n = len(tablica)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    return tablica

with open('przyklad.txt', 'r') as f:
    dane = [line.strip() for line in f]

odpowiedzi = []
naj = 0

for i in range(len(dane)):
    anagram = dane[i]
    if len(anagram) != 8:
        continue
    temp = list(anagram)
    tempn = temp.copy()
    temps = bombelkowe(temp)
    licznik = 0
    chwilowka = []
    for j in range(i + 1, len(dane)):
        tempv2 = list(dane[j])
        tempv2n = tempv2.copy()
        if tempn == tempv2n:
            continue
        tempv2s = bombelkowe(tempv2)
        if temps == tempv2s:
            licznik += 1
            chwilowka.append(dane[j])
    if licznik > 0:
        odpowiedzi.append(anagram)

#Nie mam pojęcia dlaczego jest ich za dużo NAPRAWDĘ

for x in odpowiedzi:
    print(x)
