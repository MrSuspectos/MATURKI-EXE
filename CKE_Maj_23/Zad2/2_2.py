def sprawdzanie_blokow(n):
    blocks = 0
    current_block = None

    for digit in n:
        if digit == '1':
            if current_block != '1':
                current_block = '1'
                blocks += 1
        else:
            if current_block != '0':
                current_block = '0'
                blocks += 1
    return blocks


with open('bin.txt') as file: liczby_binarne = [line.strip() for line in file]

splniajace_zalozenia = []
for x in liczby_binarne:
    if sprawdzanie_blokow(x) <= 2:
        splniajace_zalozenia.append(x)
        print(x)
print(len(splniajace_zalozenia))