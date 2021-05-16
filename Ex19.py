#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
a1 = input('Aluno 1:')
a2 = input('Aluno 2:')
a3 = input('Aluno 3:')
a4 = input('Aluno 4:')
sorteio = [a1,a2,a3,a4]
escolhido = choice(sorteio)
print(f'O escolhido foi:{escolhido}') 