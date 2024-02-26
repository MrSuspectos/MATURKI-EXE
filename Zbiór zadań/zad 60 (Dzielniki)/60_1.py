with open('liczby.txt', 'r') as file: liczby = [line.strip() for line in file]

ponizej_1000 = []
for x in liczby:
    if int(x) < 1000:
        ponizej_1000.append(x)
print(ponizej_1000[-2:])
print(len(ponizej_1000))