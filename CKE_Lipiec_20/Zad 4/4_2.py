with open('identyfikator.txt','r') as f: dane = [line.strip() for line in f]

odp = []
for identyfikator in dane:
    cz_1 = identyfikator[3:]
    cz_2 = identyfikator[:3]
    if cz_1 == cz_1[::-1] or cz_2 == cz_2[::-1]: odp.append(identyfikator)

for x in odp:print(x)