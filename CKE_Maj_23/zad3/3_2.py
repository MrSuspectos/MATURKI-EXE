#Najbardziej niezrozumiałe zadanie jakie mogli wymysleć. To zadanie nie ma sensu kiedy patrzymy na przykład.

with open('pi.txt') as file: tablica_wszystkich = [line.strip() for line in file]

tablica_2 = []
for i in range(len(tablica_wszystkich)-1):
    tablica_2.append(tablica_wszystkich[i]+tablica_wszystkich[i+1])

licznik = 0
min_ilosc = [1000,0]
max_ilosc = [0,0]
for x in range(len(tablica_2)):
    przeliczone = tablica_2.count(str(x))
    if przeliczone < min_ilosc[0] and przeliczone != 0:
        min_ilosc.clear()
        min_ilosc.append(przeliczone)
        min_ilosc.append(licznik)
    if przeliczone > max_ilosc[0]:
        max_ilosc.clear()
        max_ilosc.append(przeliczone)
        max_ilosc.append(licznik)
    licznik += 1
print(f'Najmniejsza liczba', min_ilosc[1],'wystąpień: ', min_ilosc[0])
print(f'Największa liczba', max_ilosc[1],'wystąpień: ', max_ilosc[0])