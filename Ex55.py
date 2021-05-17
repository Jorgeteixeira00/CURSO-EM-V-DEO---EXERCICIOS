#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
Maior = 0
Menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}° pessoas:'.format(p)))
    if p == 1:
        Maior = peso
        Menor = peso
    else:
        if peso > Maior:
            Maior = peso
        if peso < Menor:
            Menor = peso
print(f'O maior peso é:{Maior}')
print(f'O menor peso é:{Menor}')