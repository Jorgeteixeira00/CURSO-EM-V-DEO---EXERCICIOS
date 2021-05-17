#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opçao = 0

while opçao != 5:
    sleep(1)
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    opçao = int(input('Sua opção:'))
    
    if opçao == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif opçao == 2:
        mult = n1 * n2
        print(f'{n1} * {n2} = {mult}')
    elif opçao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print('Os dois são iguais!')
    elif opçao == 4:
        n1 = int(input('Primeiro número:'))
        n2 = int(input('Segundo número:'))
    else:
        print('OPÇÃO INVÁLIDA!')
print('FIM DO PROGRAMA!')