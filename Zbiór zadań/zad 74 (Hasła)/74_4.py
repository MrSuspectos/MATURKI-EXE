with open('hasla.txt','r') as file: hasla = [line.strip() for line in file]

spelniajace = []
for haslo in hasla:
    licznik_a = 0
    licznik_b = 0
    licznik_c = 0
    for x in haslo:
        if x.isdigit():licznik_a += 1
        if x.islower():licznik_b += 1
        if x.isupper():licznik_c += 1
    if licznik_c > 0 and licznik_b > 0 and licznik_a > 0: spelniajace.append(haslo)

print(spelniajace)
print(len(spelniajace))