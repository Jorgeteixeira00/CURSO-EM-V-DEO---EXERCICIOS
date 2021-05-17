#Exercício Python 050: Desenvolva um programa que leia seis números inteiros
#e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for x in range(1,7):
    n = int(input(f'Digite o {x}° valor:'))
    if n % 2 == 0:
        cont += 1
        soma += n
print(f'A soma entre {cont} os valores é:{soma}')