# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu sálario:'))

if salario <=1250:
    aumento = salario * 15 / 100
    novo_salario = salario + aumento
    print('Seu novo sálario com um ajuste de 15% fica R$:{}'.format(novo_salario))
else:
    aumeto = salario * 10 / 100
    novo_salario = salario + aumento
    print('Seu novo salário com um ajuste de 10% fica R$:{}'.format(novo_salario))