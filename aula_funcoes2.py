"""help(input)

help(print.__doc__)

def contador(i, f, p):
  

    i = início da contagem
    f = final da contagem
    p = passo incremental da contagem

    c = 1
    while c<=1:
        print(f'{c}', end = ' ')
        c +=p
    print('FIM!')


help(contador)




def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é {s}')



soma(3,5,6)
soma(3,5)

"""

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s



resp = soma(3,5,6)
print(resp)
print(soma(3,5))

