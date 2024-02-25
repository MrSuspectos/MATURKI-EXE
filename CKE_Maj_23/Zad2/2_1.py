def sprawdzanie_blokow(n):
    binarka = ''
    while n > 0:
        binarka += str(n % 2)
        n = n // 2

    blocks = 0
    current_block = None

    for digit in binarka:
        if digit == '1':
            if current_block != '1':
                current_block = '1'
                blocks += 1
        else:
            if current_block != '0':
                current_block = '0'
                blocks += 1

    return blocks


print(sprawdzanie_blokow(67))