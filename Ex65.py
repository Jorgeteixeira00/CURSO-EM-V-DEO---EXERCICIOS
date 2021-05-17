#Exercício Python 065: Crie um programa que leia vários números
#inteiros pelo teclado. No final da execução, mostre a média
#entre todos os valores e qual foi o maior e o menor valores
#lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = cont = media = maior = menor = 0
maior 
while resp in 'S': 
    num = int(input('Digite um número:'))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S] [N]:')).strip().upper()[0]
media = soma / cont
print('Você digitou {} número e a média foi {}'.format(cont,media))
print(f'O maior número é {maior} e o menor número é o {menor}')