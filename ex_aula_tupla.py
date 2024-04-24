
"""
Exercicio 1

a = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

n = int(input('Digite o número que gostaria de localizar (de 0 a 20): '))

p = a.index(n)


if n in a:
    print(f'O número {n} está na posição {p} da tupla')
else:
    print(f'O número {n} não faz parte dos itens dessa tupla')
    n = int(input('Digite novamente o número que gostaria de localizar (de 0 a 20): '))



lista_campeoes = ('Atlético-MG', 'Fluminense', 'Internacional', 'América-MG', 'Atlético-GO', 'Ceará', 'Bahia', 'Botafogo', 'Chapecoense')

print(lista_campeoes[:6])
print(lista_campeoes[4:9])
print(sorted(lista_campeoes))
print(lista_campeoes.index('Chapecoense'))

Exercicios 2


import random

numeros=list()

for i in range (5):
    numero = random.randint(1, 100)
    numeros.append(numero)

lista = tuple(numeros)
print(lista)

tipo_lista = type(lista)

print(tipo_lista)

print(f'O menor número da tupla é {min(lista)}')
print(f'O maior número da tupla é {max(lista)}')




Exercicio 3

lista = list()

for n in range (0,5):
    n = int(input('Digite um número: '))
    lista.append(n)

tupla = tuple(lista)

cont = 0

for item in tupla:
    if 9 == item:
        cont = cont + 1

for item in tupla:
    if item == 3:
        pos = tupla.index(item)

pares = list()

for item in tupla:
    if item % 2 == 0:
        pares.append(item)


print(f'Temos o número 9 aparecendo em {cont} componentes dessa tupla.')
print(f'O número 3 está na posição {pos}.')
print(f'Os números pares são: {pares}.')

"""



