def czy_pierwsza(n):
    dzielniki = 0
    for i in range(1,n+1):
        if n % i == 0: dzielniki += 1
    return True if dzielniki == 2 else False

with open('punkty.txt','r') as f:
    punkty = []
    for line in f:
        a,b = map(int,line.strip().split(' '))
        punkty.append([a,b])

odpowiedz = 0
for wskazane in punkty:
    if czy_pierwsza(wskazane[0]) and czy_pierwsza(wskazane[1]): odpowiedz += 1
print(odpowiedz)