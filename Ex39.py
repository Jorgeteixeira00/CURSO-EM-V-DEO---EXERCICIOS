#Exercício Python 039: Faça um programa que leia o ano
#de nascimento de um jovem e informe, de acordo com a
#sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do
#alistamento. Seu programa também deverá mostrar o tempo que
#falta ou que passou do prazo.

from datetime import date

atual = date.today().year
nasc = int(input('Digite seu ano de nascimento:'))
idade = atual - nasc

if idade == 18:
    print('Você tem {} anos!'.format(idade)) 
    print('Esta na hora de se alistar!')
elif idade > 18:
    falta = idade - 18
    print('Você tem {} anos!'.format(idade))
    print('Já passou {} anos desde seu alistamento!'.format(falta))
elif idade < 18:
    falta = 18 - idade
    print('Você tem {} anos!'.format(idade))
    print('Faltam {} anos para seu alistamento!'.format(falta))