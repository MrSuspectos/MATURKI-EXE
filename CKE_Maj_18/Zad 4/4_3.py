with open('sygnaly.txt','r') as f: sygnaly = [line.strip() for line in f]

odpowiednie = []
for sygnal in sygnaly:
    zadanie = True
    for i in range(len(sygnal)):
        syg_a = ord(sygnal[i])
        for j in range(len(sygnal)):
            syg_b = ord(sygnal[j])
            tab = [syg_a, syg_b]
            tab.sort()
            if (tab[1] - tab[0]) > 10:
                print(tab[1] - tab[0])
                zadanie = False
                break
        if not zadanie:break
    if zadanie:
        odpowiednie.append(sygnal)

for x in odpowiednie:print(x)


# zadanie wykonane na 2 punkty 
# with open('sygnaly.txt','r') as f: sygnaly = [line.strip() for line in f]

# odpowiednie = []
# for sygnal in sygnaly:
#     zadanie = True
#     for char in range(0,len(sygnal)-1):
#         tab = [ord(sygnal[char]),ord(sygnal[char+1])]
#         tab.sort()
#         if (tab[1] - tab[0]) > 10:
#             zadanie = False
#     if zadanie:
#         odpowiednie.append(sygnal)

# for x in odpowiednie:print(x)

# print(len(odpowiednie))