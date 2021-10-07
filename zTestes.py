import math

SOMATORIA = 10


def exp(base:float, exp:int) -> float:
    return base**exp

def fatorial(n:int) -> int:
    soma = 1
    while n > 1:
        soma *= n
        n -= 1
    return soma
    ## return math.factorial(n)
    ## return 1 if n > 1 else fatorial(n-1) * n


def conta(ang, n, x) -> float:
    return exp(-1, n)/fatorial(2*n if x==0 else 2*n+1) * exp(ang, 2*n + x)
    
def cosseno(ang, n) -> float:
    if n == 0:
        return conta(ang, n, 0)
    return conta(ang, n, 0) + cosseno(ang, n-1)

def sen(ang, n) -> float:
    if n == 0:
        return conta(ang, n, 1)
    return conta(ang, n, 1) + sen(ang, n-1)


def rad(ang) -> float:
    return ang*math.pi/180

print(f"cos = {cosseno(rad(30), SOMATORIA)}")
print(f"sen = {sen(rad(30), SOMATORIA)}")





"""
# float : string
teste = {}

teste[0.9] = "Pinho"
teste[0.3] = "Gui"

print(teste)
print(teste.keys())
print(teste.values())
"""






"""
fatorial = lambda n: 1 if n == 1 else fatorial(n-1) * n

print(fatorial(4))

def fatorial(n:int) -> int:
    return 1 if n == 1 else fatorial(n-1) * n

print(fatorial(4))
"""