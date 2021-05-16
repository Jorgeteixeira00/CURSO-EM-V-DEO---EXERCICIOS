#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento . 

salario = float(input('Digite o seu sálario R$:'))
aumento = salario * 15 / 100
novo_salario = salario + aumento
print('Seu antigo sálario de R${} reais com um aumento de 15% fica R${:.2f} reais.'.format(salario,novo_salario))