# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('1° primeiro número:'))
n2 = int(input('2° segundo número:'))
n3 = int(input('3° terceiro número:')) 

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')