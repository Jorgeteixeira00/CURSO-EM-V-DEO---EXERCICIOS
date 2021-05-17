#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
totMaior = 0
totMenor = 0
from datetime import date
atual = date.today().year
for c in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu:'.format(c)))
    idade = atual - nasc
    if idade <18:
        totMenor += 1
    else:
        totMaior += 1
print(f'{totMaior} pessoas são de maior!')
print(f'{totMenor} pessoas são de menor!')