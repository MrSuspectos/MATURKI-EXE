def etap_1(n):
    s_nieparzystych = 0
    s_parzystych = 0
    for i in range(len(n)):
        if i % 2 == 0: s_parzystych += int(n[i])
        else: s_nieparzystych += int(n[i])
    return s_parzystych*3, s_nieparzystych

with open('kody.txt','r') as f: dane = [line.strip() for line in f]

for kody in dane:
    print(etap_1(kody[::-1]))