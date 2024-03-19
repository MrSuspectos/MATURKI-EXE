def czy_mniejszy(n,s,k1,k2):
    i = k1
    j = k2
    n = int(n)
    while i <= n and j <= n:
        if s[i-1] == s[j-1]:
            i += 1
            j += 1
        else: return 'TAK' if s[i-1] < s[j-1] else "NIE"
    return "TAK" if j <= n else "NIE"

with open('slowa1.txt', 'r') as file:
    dane = [line.strip() for line in file]
    a, b = map(int, dane.pop().split())
    dane.append(a)
    dane.append(b)
print('slowa1.txt',czy_mniejszy(dane[0], dane[1], dane[2], dane[3]))
dane.clear()
with open('sufiks_2.txt', 'r') as file:
    dane = [line.strip() for line in file]
    a, b = map(int, dane.pop().split())
    dane.append(a)
    dane.append(b)
print('slowa2.txt',czy_mniejszy(dane[0], dane[1], dane[2], dane[3]))
dane.clear()
with open('slowa3.txt', 'r') as file:
    dane = [line.strip() for line in file]
    a, b = map(int, dane.pop().split())
    dane.append(a)
    dane.append(b)
print('slowa3.txt',czy_mniejszy(dane[0], dane[1], dane[2], dane[3]))