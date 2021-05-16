#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite o ângulo:'))

seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print(f'O Seno de {ang} é:{seno:.2f}')
print(f'O Cosseno de {ang} é:{cosseno:.2f}')
print(f'A Tangente de {ang} é:{tangente:.2f}') 