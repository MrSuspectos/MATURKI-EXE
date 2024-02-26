with open('pary.txt','r') as file:
    kochane_pary_brak_ich = []
    for x in file:
        a,b = map(str, x.split())
        kochane_pary_brak_ich.append([int(a),b])

tablica = []
for x in range(len(kochane_pary_brak_ich)):
    if kochane_pary_brak_ich[x][0] == len(kochane_pary_brak_ich[x][1]):
        if (kochane_pary_brak_ich[x][0] < kochane_pary_brak_ich[x-1][0]) or kochane_pary_brak_ich[x][0] == kochane_pary_brak_ich[x-1][0] and kochane_pary_brak_ich[x][1] < kochane_pary_brak_ich[x-1][1]:
            tablica.append(kochane_pary_brak_ich[x])
print(min(tablica))