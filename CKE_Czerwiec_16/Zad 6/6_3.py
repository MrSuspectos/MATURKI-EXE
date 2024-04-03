with open('liczby.txt','r') as f: dane = [line.strip() for line in f]

parzyste_binarne = 0
for liczba in dane:
    if liczba[-1] == '2':
        zamieniona = int(liczba[:-1])
        if zamieniona % 2 == 0: parzyste_binarne += 1

print(parzyste_binarne)