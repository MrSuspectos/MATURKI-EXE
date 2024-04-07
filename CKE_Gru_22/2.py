N = 10

def rysuj(x):
    if 2 *x <= N:
        print(x,2*x,'L')
        rysuj(2*x)
    if 2 * x + 1 <= N:
        print(x, 2 * x + 1,'P')
        rysuj(2 * x + 1)

print(rysuj(1))