with open('liczby.txt','r') as f: dane = [line.strip() for line in f]

odp = []
for liczba in dane:
    odbicie = liczba[::-1]
    odp.append([abs(int(liczba)-int(odbicie)), liczba, odbicie])

print(max(odp))