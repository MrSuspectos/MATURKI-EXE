with open('przyklad.txt','r') as f: dane = [line.strip() for line in f]

odpowiedz = []
for slowo in dane:
    temp = [char for char in slowo]
    for x in range(65,91):
        temp.append(chr(x))
        if temp == temp[::-1]:
            odpowiedz.append(temp[25])
            break
        temp.pop()
        temp.insert(0,chr(x))
        if temp == temp[::-1]:
            odpowiedz.append(temp[25])
            break
        temp.remove(chr(x))
print("".join(odpowiedz))