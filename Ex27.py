#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome:')).strip()
nome = n.split()
print('Muito prazer')
print('Seu primeiro nome é:{}'.format((nome[0])))
print('Seu ultimo nome é:{}'.format(nome[len(nome)-1])) 