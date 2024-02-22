with open('hasla.txt','r') as file: hasla = [line.strip() for line in file]

licznik = 0
for x in hasla:
    orientacja = False
    for i in range(3,len(x)):
        xd = []
        a = int(ord(x[i]))
        b = int(ord(x[i-1]))
        c = int(ord(x[i-2]))
        d = int(ord(x[i-3]))
        xd.append(a)
        xd.append(b)
        xd.append(c)
        xd.append(d)
        posortowane = sorted(xd)
        if (posortowane[0] == posortowane[1] - 1 and posortowane[1] == posortowane[2] - 1
                and posortowane[2] == posortowane[3] - 1):
            orientacja = True
    if orientacja:
        licznik += 1

print(licznik)