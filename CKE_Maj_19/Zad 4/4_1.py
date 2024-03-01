def silnia(n): return n*silnia(n-1) if n>1 else 1

with open('liczby.txt', 'r') as f: liczby = [line.strip() for line in f]

spelniajace = []
for liczba in liczby:
    wynik = 0
    for x in liczba: wynik += silnia(int(x))
    if wynik == int(liczba): spelniajace.append(liczba)

print(spelniajace)