# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.O programa deverá escrever na tela se o usuário venceu ou perdeu.

#Importei a biblioteca Random e a função randint que randomiza um número inteiro que aí foi de 1 a 5
from random import randint

#Aqui criei um variavel computador para armazenar o randint
computador = randint(1,6)


print('''
Vamos jogar um jogo?
Tente acertar um número que eu pensei
Vamos lá
''')
jogador = int(input('Seu palpite:'))

#Se o número do computador for igual ao meu palpite eu ganho, se não, eu perco
if computador == jogador:
    print('Parabéns, Você acertou!')
else:
    print('Que pena, você não conseguiu!')