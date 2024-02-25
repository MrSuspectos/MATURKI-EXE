with open('pi.txt') as file: tablica_wszystkich = [line.strip() for line in file]

tablica_2 = []
for i in range(len(tablica_wszystkich)-1):
    tablica_2.append(tablica_wszystkich[i]+tablica_wszystkich[i+1])

licznik = 0
for x in tablica_2:
    if int(x) > 90:
        licznik += 1
print(licznik)