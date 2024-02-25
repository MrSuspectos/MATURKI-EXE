def czy_pierwsza(x):
    if x < 2: return False
    temp = []
    for i in range(1, x+1):
        if x % i == 0: temp.append(i)
    if len(temp) == 2: return True
    return False

with open('trojki.txt','r') as file:
    trojki = []
    for line in file:
        a,b,c = map(int, line.split())
        trojki.append([a,b,c])

poprawne = []
for x in trojki:
    war_a = czy_pierwsza(x[0])
    war_b = czy_pierwsza(x[1])
    if war_a and war_b and x[0] * x[1] == x[2]: poprawne.append(x)


print(poprawne)
print(len(poprawne))