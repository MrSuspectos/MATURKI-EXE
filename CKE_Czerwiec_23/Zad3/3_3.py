with open('anagram.txt','r') as f: dane = [line.strip() for line in f]

naj = 0
for x in range(len(dane)-1):
    a = int(dane[x],2)
    b = int(dane[x+1],2)
    if abs(a-b) > naj: naj = abs(a-b)

print(bin(naj)[2:])