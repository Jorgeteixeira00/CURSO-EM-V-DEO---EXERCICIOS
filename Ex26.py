# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e 
# mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

f = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes nessa frase'.format(f.count('A')))
print('A mesma letra aparece pela primeira vez na posição {}'
      ' e pela última na {}'.format(f.find('A')+1,f.rfind('A')+1))
