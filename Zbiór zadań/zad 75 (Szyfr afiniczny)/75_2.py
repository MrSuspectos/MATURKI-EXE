def zamiana_na_liczby(A,B,kochany_tekst):
    a = A
    b = B
    zwroconytekst = []
    for x in kochany_tekst: zwroconytekst.append(ord(x)-97)
    tekst = ''
    for y in zwroconytekst:
        liczba = y * a + b
        if liczba > 25: liczba = liczba % 26
        tekst += chr(liczba+97)
    return tekst

with open('tekst.txt','r') as f: tekst = [line.strip().split(' ') for line in f]

zwrocone = []
for x in tekst:
    for y in x:
        if len(y) >= 10: zwrocone.append(zamiana_na_liczby(5,2,y))

for x in zwrocone: print(x)