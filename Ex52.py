#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont = 0
tot = 0
n = int(input('Digite um número:'))
for c in range(1,n+1):
    if n % c == 0:
        print('\033[32m',end=' ')
        cont +=1
        tot += 1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c), end=' ')
print('\nEle foi dívisivel {} vezes!'.format(tot))
if cont == 2:
    print('Ele é um número primo!')
else:
    print('Ele não é um número primo!')