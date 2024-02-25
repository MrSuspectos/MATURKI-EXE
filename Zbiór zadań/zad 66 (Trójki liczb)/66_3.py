with open('trojki.txt','r') as file:
    trojki = []
    for line in file:
        a,b,c = map(int, line.split())
        trojki.append(sorted([a,b,c]))

zgodne_z_zadaniem = []
for i in range(len(trojki)-1):
    #ciekawe!
    if trojki[i][0]**2 + trojki[i][1]**2 == trojki[i][2]**2 and trojki[i+1][0]**2 + trojki[i+1][1]**2 == trojki[i+1][2]**2:
        zgodne_z_zadaniem.append(trojki[i])
        zgodne_z_zadaniem.append(trojki[i+1])

print(zgodne_z_zadaniem)
print(len(zgodne_z_zadaniem))