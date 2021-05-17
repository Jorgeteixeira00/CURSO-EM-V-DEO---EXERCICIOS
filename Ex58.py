#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai
#"pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
#adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
palpites = 0
from random import randint
computador = randint(1,10)

print('''
Vamos jogar um jogo?
Tente acertar um número que eu pensei entre 1 e 10
''')
jogador = int(input('Qual o seu palpite?'))
while jogador != computador:
    if jogador > computador:
        print('Menos... Tente novamente')
        jogador = int(input('Qual o seu palpite?'))
        palpites += 1
    else:
        print('Mais... Tente novamente')
        jogador = int(input('Qual o seu palpite?'))
        palpites += 1
print(f'Com {palpites} tentativas você conseguiu acertar!')