#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. 

frase = input('Digite algo:')
print('O tipo primitivo desse valo é:',type(frase))
print('Só tem espaços?', frase.isspace())
print('É um número?', frase.isalnumeric())
print('É alfabético?', frase.isalpha())
print('É alfanumérica?', frase.isalnum())
print('Está em maiusculo?', frase.upper())
print('Está em minusculo?', frase.lower())
print('Está Capitalizada?', frase.title())