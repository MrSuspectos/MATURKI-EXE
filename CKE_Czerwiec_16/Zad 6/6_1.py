with open('liczby.txt','r') as f: dane = [line.strip() for line in f]

osemkowe = 0
for liczba in dane:
    if liczba[-1] == '8': osemkowe += 1
print(osemkowe)