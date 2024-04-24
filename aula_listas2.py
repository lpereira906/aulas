teste = list()
teste.append("Gustavo")
teste.append(40)
galera=list()
galera.append(teste[:])
teste[0]="Maria"
teste[1]=22
galera.append(teste[:])
print(teste)
print(galera)
galera2=[["João", 19], ["Ana",33], ["Joaquim",13], ["Maria", 45]]
print(galera2[2][1])

for pessoa in galera:
    print(pessoa)

for pessoa in galera:
    print(pessoa[0])

for pessoa in galera:
    print(pessoa[1])

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

for pessoa in galera2:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

galera3=list()
dado=list()
totmai = totmen = 0

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear()

print(galera3)

for p in galera3:
    if p[1]>=21:
        totmai +=1
    else:
        totmen +=1
print(totmai)
print(totmen)
