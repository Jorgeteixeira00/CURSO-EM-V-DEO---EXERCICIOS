#Exercício Python 056: Desenvolva um programa que leia o nome,
#idade e sexo de 4 pessoas. No final do programa, mostre:
#a média de idade do grupo, qual é o nome do homem mais velho
#e quantas mulheres têm menos de 20 anos.
somaIdade = 0
mediaIdade = 0
maiorIdadehomem = 0
homemVelho = ''
totMulher20 = 0
for p in range(1,5):
    print('{}° PESSOA'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M] [F]:')).upper().strip()
    somaIdade += idade
    if p == 1 and sexo in 'M':
        maiorIdadehomem = idade
        homemVelho = nome
    if sexo in 'M' and idade > maiorIdadehomem:
        maiorIdadehomem = idade
        homemVelho = nome
    if sexo in 'F' and idade <20:
        totMulher20 += 1
mediaIdade = somaIdade / 4
print('A média das idades é {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadehomem,homemVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totMulher20))