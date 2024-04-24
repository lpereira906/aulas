"""
def mostralinha():
    print('--------------------------------------')


def mostralinha():
    print('-'*36)

def mensagem (msg):
    print('-'*36)
    print(msg)
    print('-'*36)


#Programa principal (manter duas linhas de distancia das funcoes)    

mostralinha()
print('        SISTEMA DE ALUNOS       ')
mostralinha()
mostralinha()
print('        CADASTRO DE FUNCIONÁRIOS       ')
mostralinha()
mostralinha()
print('        ERRO DE SISTEMA       ')
mostralinha()

mostralinha()
mensagem('SISTEMA DE ALUNOS')
mostralinha()

def contador(* núm):
    for valor in núm:
        print(valor, end=' ')
    print('FIM!')

def contagem(*núm):
    for valor in núm:
        print(f'A contagem tem {len(núm)} componentes.')
    

contador(1, 2, 3, 4, 5)
contagem(1, 2, 3)
contagem(1, 2)
"""


#Função dobra

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1

#Função Soma

def soma(*valores):
    s = 0
    for núm in valores:
        s+= núm
    print(s)


lst = [2, 5, 6, 8, 9]

dobra(lst)
print(lst)

soma(4, 5, 3, 1)
