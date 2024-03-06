with open('sygnaly.txt','r') as file: sygnaly = [line.strip() for line in file]

wyraz = ""
for linia in range(39, len(sygnaly),40): wyraz += sygnaly[linia][9]

print(wyraz)