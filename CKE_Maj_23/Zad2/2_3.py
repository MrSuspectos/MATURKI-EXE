with open('bin.txt') as file: binarne = [line.strip() for line in file]

najwieksza = 0
for x in binarne:
    liczba = int(x,2)
    if liczba > najwieksza:
        najwieksza = liczba

print(bin(najwieksza)[2:])