
"""
locadora=list()
file={}
filme1 = {'titulo':'Star Wars', 'ano':1977, 'diretor':'Goerge Lucas'}
filme2 = {'titulo':'Avangers', 'ano':2012, 'diretor':'Jass Whedan'}
filme3 = {'titulo':'Matrix', 'ano':1999, 'diretor':'Wachowski'}
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
print(filme1.values())
print(filme1.keys())
print(filme1.items())

for k,v in filme1.items():
    print(k,v)

print(locadora[0]['ano'])
print(locadora[2]['titulo'])


pessoas={'nome': 'Gustavo', 'sexo':'M', 'idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} e é do sexo {pessoas["sexo"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k,v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']

print(pessoas)

pessoas['nome'] = 'Leandro'
print(pessoas)

pessoas['peso'] = 85
print(pessoas)



estado1={'Estado': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2={'Estado': 'São Paulo', 'sigla': 'SP'}
estado3={'Estado': 'Espírito Santo', 'sigla': 'ES'}
lista_estado=list()
lista_estado.append(estado1)
lista_estado.append(estado2)
lista_estado.append(estado3)

print(lista_estado)
print(lista_estado[0])
print(lista_estado[1]['sigla'])

"""

estado={}
brasil=list()

for c in range(0,3):
    estado['uf'] = str(input('Digite a unidade federativa: '))
    estado['sigla']=str(input('Digite a sigla: '))
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    print(e)
    for k, v in e.items():
        print(f'{k} = {v}')