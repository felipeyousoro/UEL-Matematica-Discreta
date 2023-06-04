import random
import os
import sys
def pemsi(phi):
    e = 2
    while(mdc(e, phi) != 1):
        e = e + 1
    return e

def mdc(x, y):
    while (y != 0):
        x, y = y, x % y
    return x

def bakuretsu(e, phi):
    d = pow(int(e), -1, int(phi))
    return int(d)

def megumin(msg, n, e):
    explosion = pow(msg, e, n)
    return explosion


def descripto(msg, d, num, N):
    ds = []
    ms = []
    MSG = 0
    for n in range(0, len(num)):
        ds.append(d % (num[n]-1))
        ms.append(pow(msg, ds[n]) % num[n])
        MSG = MSG + (N//num[n]) * ms[n] * pow(int(N/num[n]), -1, int(num[n]))

    MSG = MSG % N
    return MSG


aqv = open(os.path.join(sys.path[0], "primos.txt"), "r") 

num = []
geral = []
speweek = []
n = 1
phi = 1

#MUDAR A QUANTIDADE DE PRIMOS UTILIZADOS AQUI
#
#
#
quantidade_de_primos = 4
#
#
#
#MUDAR A QUANTIDADE DE PRIMOS UTILIZADOS AQUI

for f in aqv:
    speweek.append(int(f))
for f in range(quantidade_de_primos):
    r = random.randint(0, len(speweek) - 1)
    num.append(speweek[r])
    speweek.remove(speweek[r])
for k in num:
    n = k * n
msg = random.randint(0, n//2)
for k in num:
    phi = phi * (k - 1)

e = pemsi(phi)
d = bakuretsu(e, phi)
segredo = megumin(msg, n, e)
desc = descripto(segredo, d, num, n)

print('Números:', num)
print("Phi:", phi)
print("Chave Publica: <%s, %s>" %(n, e))
print("Chave Privada: <%s, %s>" %(n, d))
print('Mensagem:', str(msg))
print('Mensagem Cripto:', segredo)
print('Mensagem Descripto:', desc)
input("Pressione enter para sair...")
aqv.close()