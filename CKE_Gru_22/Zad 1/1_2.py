with open('mecz.txt','r') as f: dane = [line.strip() for line in f.readline()]

punktyA = 0
punktyB = 0
for i in range(0,10000):
    if dane[i] == 'A': punktyA += 1
    else: punktyB += 1
    if punktyA >= 1000 or punktyB >= 1000:
        check = punktyA - punktyB
        if check >= 3:
            print('A', punktyA, '/', punktyB)
            break
        if check <= -3:
            print('B', punktyA, '/', punktyB)
            break