with open('liczby.txt','r') as f: dane = [line.strip() for line in f]

for liczba in dane:
    if int(liczba[::-1]) % 17 == 0: print(liczba[::-1])