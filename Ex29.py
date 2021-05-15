#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Digite a velocidade do carro:')) # A varivel de velocidade
if vel > 80: # Se ele passar de 80km
    multa = vel - 80 #Aqui é o excesso
    preço_da_multa = multa * 7 #Aqui é o preço a se pagar, pegando o excesso e multiplicando pelo preço da multa que é 7.00 reais 
    print('Você foi multado com uma multa de R${:.2f} reias'.format(preço_da_multa))
    print('Tenha um bom dia e dirija com segunrança!')
else:
    print('Tenha um bom dia e diriga com segurança!')