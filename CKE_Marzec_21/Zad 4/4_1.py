with open('galerie.txt', 'r') as f: dane = [line.split() for line in f]

odpowiedzi = {}
for galeria in dane:
    slowo = galeria[0]
    if slowo in odpowiedzi:
        odpowiedzi[slowo] += 1
    else:
        odpowiedzi[slowo] = 1

for slowo, count in odpowiedzi.items():
    print(slowo, count)
