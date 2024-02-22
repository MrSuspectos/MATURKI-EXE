with open('hasla.txt','r') as file: hasla = [line.strip() for line in file]

licznik = 0
for x in hasla:
    if x.isdigit(): licznik += 1
print(licznik)