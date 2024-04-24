"""
Exercicio 1

pessoas = list()
listapesados=list()
listaleves=list()
pesados = leves = 0

nomes = list()
pesos = list()

nomes.append(str(input('Digite o nome da pessoa: ')))
pesos.append(int(input('Digite o peso da pessoa: ')))
decisao = str(input('Deseja incluir mais uma pessoa? (s/n)'))

while decisao == 's':
    nomes.append(str(input('Digite o nome da pessoa: ')))
    pesos.append(int(input('Digite o peso da pessoa: ')))

    decisao = str(input('Deseja incluir mais uma pessoa? (s/n)'))

contagem = len(nomes)

for i in range(contagem):
    if pesos[i] >= 85:
        pesados += 1
        listapesados.append((nomes[i], pesos[i]))
    else:
        leves +=1
        listaleves.append((nomes[i], pesos[i]))

print(f'O númeto de pessoas cadastradas foi {contagem}')
print(f'O número de pessoas acima do peso é {pesados}, sendo eles: {listapesados}')
print(f'O número de pessoas de peso ideal é {leves}, sendo eles: {listaleves}')


Exercicio 2

numeros = list()

pares = list()
impares=list()

for i in range (7):
    numeros.append(int(input('Digite um número: ')))

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort()

print(f'A lista de números digitados é: {numeros}')
print(f'A lista de números pares são: {pares}')
print(f'A lista de números ímpares são: {impares}')


Exercico 3

linhas = 3
colunas = 3
somapares = 0
somaterceira = 0
maiorvalor = 0
segundalinha = list()

matriz = [[0 for i in range (linhas)] for j in range (colunas)]

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = int(input(f'Insira o número de linha {i}, coluna {j}:  '))

for i  in range(linhas):
    for j in range (colunas):
        if matriz[i][j] %2 == 0:
            somapares = somapares + matriz[i][j]

for i  in range(linhas):
    for j in range (colunas):
        if j == 2:
            somaterceira = somaterceira + matriz[i][j]

for i  in range(linhas):
    for j in range (colunas):
        if i == 1:
            segundalinha.append(matriz[i][j])

maiorvalor = max(segundalinha)
    

print(f'A matriz inserida é {matriz}.')

print(f'A soma dos números pares da matriz é {somapares}.')

print(f'A soma dos números da terceira coluna é {somaterceira}.')

print(f'O maior valor da segunda linha é {maiorvalor}.')



Exercico 4

import random

listapalpite = list()
listatotal = list()
numerodeapostas = 0
numero = 0

numerodeapostas = int(input('Digite o número de apostas que deseja realizar: '))

for i in range (numerodeapostas):
    listapalpite = set()
    for j in range (6):
        numero = random.randint(1, 60)
        listapalpite.append(numero)
    listatotal.append(listapalpite[:])

print(listatotal)

"""