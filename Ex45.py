# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

computador = randint(0,2)
print(computador)

print('''
Vamos joga um jogo?
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Digite sua opção:'))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')

if jogador == 0:
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('VOCÊ PERDEU!')
    else:
        print('VOCÊ GANHOU!')

elif jogador == 1:
    if computador == 0:
        print('VOCÊ GANHOU!')
    elif computador == 1:
        print('EMPATE')
    else:
        print('VOCÊ PERDEU!')

elif jogador == 2:
    if computador == 0:
        print('VOCÊ PERDEU!')
    elif computador == 1:
        print('VOCÊ GANHOU!')
    else:
        print('EMPATE')
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE!')
print(jogador)
print(computador)