#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt
cO = float(input('Digite o cateto oposto:'))
cA = float(input('Digite o cateto adjascente:'))

hip = cO ** 2 + cA ** 2
print(f'A hipotenusa dos catetos é:{sqrt(hip):.2f}')