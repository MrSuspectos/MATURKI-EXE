def dwucyklicznosc(ciag):
    d = len(ciag)
    if d % 2 != 0:
        return False
    a = d // 2
    if ciag[:a] == ciag[a:]:
        return True
    return False

dwucykliczna_liczba = []
with open('ciagi.txt', 'r') as file:
    ciag = [line.strip() for line in file]

for x in ciag:
    if dwucyklicznosc(x):
        dwucykliczna_liczba.append(x)

for x in dwucykliczna_liczba:
    print(x)