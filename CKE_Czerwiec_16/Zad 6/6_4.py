with open('liczby.txt','r') as f: dane = [line.strip() for line in f]

wynik = 0
for liczba in dane:
    if liczba[-1] == '8':
        zamieniona = int(liczba[:-1],8)
        wynik += zamieniona
print(wynik)