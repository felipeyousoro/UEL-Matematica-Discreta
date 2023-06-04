import time
import random
import sys
sys.setrecursionlimit(1000000000)
P = 0
I = 0
R = 0
E = 0
N = 0

T = 7200

def forcabruta(valor, peso, tamanho, n, m):
    global I
    global E
    global N
    global T
    E = E + 1
    if(tamanho == 0):
        return 0
    if(m>=n):
        return 0 
    if(peso[m]>tamanho):
        return forcabruta(valor, peso, tamanho, n, m+1)
    maior = 0
    x = tamanho // peso[m]
    for i in range (x, -1, -1):
        tmp = time.time()
        if(tmp - N >= T):
            return maior

        y = forcabruta(valor, peso, tamanho - peso[m] * i, n, m+1)
        z = valor[m] * i 
        total = z + y
        maior = max(maior, total)
        I = I + 1
        
    return maior



def instintosuperior(dados, tamanho, n, m, Z):
    global P    
    global R
    global T
    global N
    R = R + 1
    if(tamanho<=0):
        return Z
    if(m>=n):
        return Z 
    if(dados[m][2]>tamanho):
        return instintosuperior(dados, tamanho, n, m+1, Z)

    x = tamanho // dados[m][2]
    hikari = Z
    for i in range (x, -1, -1):
        tmp = time.time()
        if(tmp - N >= T):
            return Z
        y = dados[m][1] * i 
        if(m+1==n):
            limite = hikari + y
        else:
            limite = hikari + y + dados[m+1][0] * (tamanho - i * dados[m][2])
        if((Z <= limite) and (m + 1 < n)):
            ZE = instintosuperior(dados, tamanho - i * dados[m][2], n, m+1, hikari+y)
        elif(Z <= limite):
            ZE = hikari + y        
        P = P + 1
        Z = max(Z, ZE)

    return Z

tamanho = 0
valor = []
peso = []
j = int(input('Quantos numeros? '))
print('Horario de inicio: ', time.strftime("%H:%M:%S"))

for i in range(0, j):
    valor.append(random.randint(50, 151))
    peso.append(random.randint(10, 51))
    tamanho = tamanho + peso[i]

tamanho = tamanho//2

n = len(valor)
print('Interesse: ', valor)
print('Peso: ',peso)
print('Tamanho: ',tamanho)

arrumar = []
for i in range(0, n):
    arrumar.append([valor[i]/peso[i], valor[i], peso[i]])
arrumar = sorted(arrumar)
for i in range(0, n//2):
   arrumar[i], arrumar[len(arrumar)-i-1] = arrumar[len(arrumar)-i-1], arrumar[i]



t = time.time()
N = t
print('Melhor caso com limite superior: ',instintosuperior(arrumar, tamanho, n, 0, 0))
#instintosuperior(arrumar, tamanho, n, 0, 0)
print("Tempo gasto com limite superior:",time.time() - t)


t = time.time()
N = t
print('Melhor caso usando força bruta: ',forcabruta(valor, peso, tamanho, n, 0))
#forcabruta(valor, peso, tamanho, n, 0)
print('Tempo gasto com força bruta:', time.time() - t)


print('Loops com limite superior: '+ str(P) + '\nLoops com forca bruta: '+ str(I))
print('Recursões com limite superior: '+ str(R) + '\nRecursoes com forca bruta: '+ str(E))
print('-----------------------------------------------------------')

print("Horario de fim: ", time.strftime("%H:%M:%S"))

input("Pressione enter para sair...")
