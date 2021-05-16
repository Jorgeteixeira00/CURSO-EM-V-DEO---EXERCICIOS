#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

#Pedir um número ao usario
num = int(input('Digite um número:'))

#Se o número tiver o resto da divisão por 2 = a 0(10/2=5 resto 0, 5/2=4 resto 1 Sacou?) Significa que ele é par 
if num % 2 == 0:
    print('Ele é par!')
else: #Se não ele é impar
    print('Ele é ímpar!')