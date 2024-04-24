#exercicio 1:
"""
lista1=[]

for cont in range(0,5):
    lista1.append(int(input('Digite um valor: ')))

print(lista1)


print(f'O maior valor da lista {lista1} é {max(lista1)} na posição {lista1.index(max(lista1))}')
print(f'O maior valor da lista {lista1} é {min(lista1)} na posição {lista1.index(min(lista1))}')
"""
# exercicio 2:
"""
lista2=[]

for cont in range(0,10):
    n = int(input('Digite um valor: '))
    if n in lista2:
        print('Número informado já consta na lista.')
    else:
        lista2.append(n)
lista2.sort()
print(lista2)

"""

# exercício3:

#método malaco
"""
import bisect

lista3=[]

for cont in range(0,5):
    n = int(input('Digite um valor: '))
    bisect.insort(lista3, n)

print(lista3)
"""

#fazendo direito genivaldo:
"""
lista3 = []

for i in range(5):
    n = int(input('Digite um valor: '))
    
    posicao = 0

    while posicao < len(lista3) and n > lista3[posicao]:
        posicao += 1

    lista3.insert(posicao, n)

print(lista3)

#mil vezes e nao saiu sem a ajuda do chatgpt esse de cima

"""
"""
lista4=[]


d = 's'

while d == 's':
    n=int(input(f'Insira um número: '))
    d = input('Deseja inserir outro número?: (s/n)')
    lista4.append(n)
    lista4.sort()
    print(lista4)

lista5.copy(lista4)
lista5.sort(reverse=True)
print(f'A lista de número digitados é: {lista4}, contendo {len(lista4)} itens, se ordenada em ordem decrescente ficará {lista5}. ')
 
if 5 in lista4:
    
    print(f'O número 5 está contido na lista.')

else:
    print(f'O número 5 NÂO está contido na lista.')
"""
"""
lista6=[]
lista_impar=[]
lista_par=[]

d = 's'

while d == 's':
    n=int(input(f'Insira um número: '))
    d = input('Deseja inserir outro número?: (s/n)')
    lista6.append(n)
    lista6.sort()
    print(lista6)

for numero in lista6:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print(f'A lista inserida é {lista6}')
print(f'A lista de números ímpares é {lista_impar}')
print(f'A lista de números pares é {lista_par}')

""" 