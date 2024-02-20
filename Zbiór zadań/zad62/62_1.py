file = open('liczby1.txt','r')

liczby = []
for line in file:
    line.strip()
    liczby.append(int(line,8))

posortowana = sorted(liczby)
print('Najmniejsza liczba: ', posortowana[0])
print('Najmniejsza liczba (osemkowo): ', oct(posortowana[0])[2:])
print('Największa liczba: ', posortowana[-1])
print('Najmniejsza liczba (osemkowo): ', oct(posortowana[-1])[2:])