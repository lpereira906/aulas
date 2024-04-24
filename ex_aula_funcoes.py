"""
Ex. 1

def area (l, c):
    a = l * c
    print(f'A área do terreno é de {a} m²')

l = float(input('Digite a Largura do terreno: '))
c = float(input('Digite o Comprimento do terreno: '))

area(l, c)


Ex. 2

def escreva(texto):
    print('-'* len(texto))
    print(texto)
    print('-'* len(texto))


escreva('Olá Mundo!')

"""

def contagem():
    pos = 1
    print('-'*10)
    while pos < 11:
        print(pos)
        pos += 1
    print('-'*10)

    pos = 10
    while pos > 0:
        print(pos)
        pos -= 1
    print('-'*10)

    print('Agora é sua vez, digite o início da contagem, o fim e o passo:')
    inicio = int(input('Digite o início da contagem: '))
    final = int(input('Digite o final da contagem: '))
    passo = int(input('Digite o passo da contagem: '))

    if inicio < final and passo > 0:
        pos = inicio
        print(pos)
        while pos + passo <= final:
            pos = pos + passo
            print(pos)
        print('FIM!')
    elif inicio > final and passo < 0:
        pos = inicio
        print(pos)
        while pos + passo >= final:
            pos = pos + passo
            print(pos)
        print('FIM!')
    else:
        print('Entrada inválida para contagem regressiva.')

contagem()