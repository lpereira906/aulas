comidas = ('Hamburguer', 'Batata', 'Refrigerante')

for pos, comida in enumerate(comidas):
    print(f'A comida da posição {pos} da lista é {comida}')

for comida in comidas:
    print(comida)

for cont in range(0, len(comidas)):
    print(f'O item {cont} da lista é {comida}')

print(sorted(comidas))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))

a = (2, 5, 4)
b = (5, 8, 1, 2)
d = b + a
print(d)
print(len(d))
print(c.count(2))
print(c.index(5))
print(c.index(5, 2))