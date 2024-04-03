with open('liczby.txt','r') as f: dane = [line.strip() for line in f]

liczb_w_dziesietnym = []
for liczba in dane:
    system = int(liczba[-1])
    zamieniona = int(liczba[:-1],system)
    liczb_w_dziesietnym.append([zamieniona, liczba])

print(max(liczb_w_dziesietnym), min(liczb_w_dziesietnym))