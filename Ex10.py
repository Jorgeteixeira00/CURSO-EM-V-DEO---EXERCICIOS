#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

valor = float(input('Digite quando você tem na carteira R$:')) 
dolar = valor*0.19
print('Com R${} reais você pode comprar US${:.2f} dólares!'.format(valor,dolar))