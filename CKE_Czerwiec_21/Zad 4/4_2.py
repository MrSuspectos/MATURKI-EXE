with open('napisy.txt','r') as f: dane = [line.strip() for line in f]

haslo = []
licznik = 0
for slowo in range(19,len(dane),20):
    haslo.append(dane[slowo][licznik])
    licznik += 1

print("".join(haslo))