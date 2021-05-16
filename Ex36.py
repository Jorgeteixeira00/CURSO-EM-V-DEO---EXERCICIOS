# Exercício Python 036: Escreva um programa para aprovar o empréstimo
#bancário para a compra de uma casa. Pergunte o valor da casa,
#o salário do comprador e em quantos anos ele vai pagar. A prestação
#mensal não pode exceder 30% do salário ou então o empréstimo será negado

valor = float(input('Digite o valor da casa:'))
salario = float(input('Digite seu sálario:'))
anos = float(input('Em quantos anos você vai pagar a casa:')) 
prestação = anos * 12
prestao_mensal = valor / prestação
excesso = salario * 30 / 100
print(f'Para pagar uma casa de R${valor} reais em {anos} anos a prestação mensal séra de R${prestao_mensal:.2f} reais')

if prestao_mensal > excesso:
    print('EMPRESTIMO NEGADO!')
else:
    print('EMPRESTIMO ACEITO!')