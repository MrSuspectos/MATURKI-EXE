with open('ciagi.txt','r') as file:
    ciag = [line.strip() for line in file]

licznik = 0
for x in ciag:
    if str(x).count('11') == 0:
        licznik += 1
print(licznik)