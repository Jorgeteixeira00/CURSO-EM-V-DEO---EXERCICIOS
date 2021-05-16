#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de km rodados:'))
dias = int(input('Digite o total de dias que você alugou o carro:'))

preço_km = km * 0.15
preço_dia = dias * 60
preço_total = preço_km + preço_dia

print('''
Total de dias alugado:{}
Total de Km rodados:{}
Preço por km rodados:{:.2f} reais
Preço por dias alugados:{:.2f} reais
Preço total:{:.2f} reais
'''.format(dias,km,preço_km,preço_dia,preço_total)) 