with open('dane_napisy.txt') as f:
    anagramy = []
    for line in f:
        a,b = map(str,line.strip().split(' '))
        anagramy.append(a)
        anagramy.append(b)

k = 0
wynik = []
licznik_anagrama = 0
for anagram in anagramy:
    licznik = 0
    tymczas = []
    for ang in range(len(anagramy)):
        if licznik_anagrama == ang:
            tymczas.append(anagram)
            continue
        if sorted(anagram) == sorted(anagramy[ang]):
            licznik += 1
            tymczas.append(anagramy[ang])
    if licznik > k:
        k = licznik
        wynik.clear()
        wynik = tymczas.copy()
    licznik_anagrama += 1

print('Najwieksza liczba to:',len(wynik),'w której skład wchodza',wynik)