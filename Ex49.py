#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para ver a tabuada:'))
for x in range(1,11):
    print('{} x {} = {}'.format(n,x,n*x))