with open('napisy.txt','r') as f: dane = [line.strip() for line in f]

licznik = 0
for slowo in dane:
    for znak in slowo:
        if znak.isdigit(): licznik += 1
print(licznik)