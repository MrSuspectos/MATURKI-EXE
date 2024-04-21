with open('liczby.txt','r') as f:
    dane = []
    for line in f:
        line = float(line)
        dane.append(line)

print('Największa',max(dane),'index:',dane.index(max(dane)) + 1)
print('Najmniejsza',min(dane),'index:',dane.index(min(dane)) + 1)