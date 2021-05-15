#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#Declarei uma variavel distancia
distancia = float(input('Digite a distância da viagem:'))

#Se a distancia for menor ou igual a 200 o preço por km vai ser de 0.50 centavos
#Se não, se for maior que 200 o preço séra de 0.45 centavos
#E em cada condição eu crio uma variavel preço e multiplico pelo preço

if distancia <=200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'''
Distância:{distancia} km
Preço total R$:{preço:.2f} reais
''')