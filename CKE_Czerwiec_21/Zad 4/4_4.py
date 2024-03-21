with open('napisy.txt', 'r') as f: dane = [line.strip() for line in f]

zmienna = False
odpowiedz = []
for slowo in dane:
    temp = []
    for x in range(len(slowo)):
        if slowo[x].isdigit(): temp.append(slowo[x])
    if len(temp) == 0: continue
    if len(temp) % 2 != 0: temp.pop()
    for x in range(0,len(temp)-1,2):
        numer = int(temp[x]+temp[x+1])
        if numer >= 65 and numer <= 90:
            odpowiedz.append(chr(int(numer)))
            if "".join(odpowiedz).endswith('XXX'):
                zmienna = True
                break
    if zmienna: break

print("".join(odpowiedz))