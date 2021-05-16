# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o preço do produto:'))
print('''
[1] Á vista dinheiro/cheque
[2] Á vista no cartão
[3] Em 2x no cartão
[4] 3x ou mais no cartão
''')
opcão = int(input('Digite sua opção:')) 

if opcão == 1:
    desconto = valor - (valor * 10 / 100)
    print('O seu produto de R${:.2f} reias, á vista no dinheiro/cheque terá um desconto de 10% e ficara por R$:{:.2f} reais'.format(valor,desconto))
elif opcão == 2:
    desconto = valor - (valor * 5 / 100)
    print('O seu produto de R${:.2f} reias, á vista no cartão terá um desconto de 5% e ficara por R$:{:.2f} reais'.format(valor,desconto))
elif opcão == 3:
    print('O seu produto de R${:.2f} reais, ficara com 2 parcelas no cartão de R${} reais'.format(valor, valor/2))
elif opcão == 4:
    vezes = int(input('Deseja parcelar em quantas vezes?'))
    valor_parcelado = valor / vezes
    valor_juros = valor_parcelado + (valor * 20  / 100)
    print('O seu produto de R${:.2f} reia, ficara com {} parcelas de R${} reais.'.format(valor,vezes,valor_juros))
else:
    print('Opção invalida, tente novamente!')
