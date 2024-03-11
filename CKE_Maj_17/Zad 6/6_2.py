with open('dane.txt', 'r') as f: linie = [line.strip().split(' ') for line in f]

do_usuniecia = 0
for i in linie:
    odwrocona = list(reversed(i))
    if odwrocona != i: do_usuniecia += 1


# Jakiś kod przypadkowego użytkownika YT
# for i in range(200):
#     if linie[i][::] != linie[i][::-1]:
#         do_usuniecia += 1

print(do_usuniecia)
