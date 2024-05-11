def etap_1(n):
    s_nieparzystych = 0
    s_parzystych = 0
    for i in range(len(n)):
        if i % 2 == 0: s_parzystych += int(n[i])
        else: s_nieparzystych += int(n[i])
    sukces = (s_parzystych*3) + s_nieparzystych
    przeliczona = sukces % 10
    return 10-przeliczona if przeliczona != 0 else przeliczona

with open('kody.txt','r') as f: dane = [line.strip() for line in f]
with open('cyfra_kodkreskowy.txt','r') as fi:
    kontrolne = []
    for line in fi.readlines()[1:]:
        a,b = map(str, line.strip().split())
        kontrolne.append(b)

for kody in dane:
    przeliczone = etap_1(kody[::-1])
    print(przeliczone, kontrolne[przeliczone])
