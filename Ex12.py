#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto R$:'))
desconto = preço * 5 / 100
print('O antigo preço com 5% de desconto fica de R${:.2f} reais.'.format(preço-desconto))