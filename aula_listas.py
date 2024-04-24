alfabeto = ['a', 'b', 'c', 'd']

print(alfabeto[0])
print(alfabeto[2])

alfabeto.append('e')

print(alfabeto[4])

alfabeto.insert(0,'A')

print(alfabeto[0])

alfabeto.pop(0)
print(alfabeto)

alfabeto.remove('e')
print (alfabeto)

alfabeto.append('f')
alfabeto.append('g')

if 'f' in alfabeto:
    alfabeto.remove('f')
print (alfabeto)

valores = list(range(4,11))
print(valores)

valores2 = [5, 8 , 6, 7, 2]
print(valores2)

valores2.sort()
print(valores2)

valores2.sort(reverse=True)
print(valores2)

print(f'A variável valores tem: {len(valores)} elementos')

print(f'A variável valores2 tem: {len(valores2)} elementos')

lista_teste=[]

for cont in range(0,5):
    lista_teste.append(int(input('Digite um valor: ')))

for c, v in enumerate(lista_teste):
       print (f'Na posição {c} encontrei o valor {v}')

z = int(input(('Insira um número a ser verificado: ')))

if z in lista_teste:
     print(f'O valor {z} pertence ao grupo da lista.')
else:
     print('Os valores encontrados são: ')
     for c, v in enumerate(lista_teste):
       print (f'Na posição {c} encontrei o valor {v}')
     print(f'Sendo que o valor {z} não consta nessa lista')

a = [lista_teste[:]]

print(a)
