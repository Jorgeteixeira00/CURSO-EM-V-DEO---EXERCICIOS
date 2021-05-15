# Exercício Python 037: Escreva um programa em Python que leia
#um número inteiro qualquer e peça para o usuário escolher
#qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número:'))
print('''
SISTEMA DE CONVERSÃO
[1] BÍNARIO
[2] OCTAL
[3] HEXADECIMAL
''')
opção = int(input('Sua opção:'))

if opção == 1:
    print('{} em BÍNARIO:{}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} em OCTAL:{}'.format(num,oct(num)[2:]))
elif opção  == 3:
    print('{} em HEXADECIMAL:{}'.format(num,hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA!')