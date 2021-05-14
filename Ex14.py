#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

C = float(input('Digite a temperatura em C°:'))
F = (C * 9/5) + 32
print('{} C° convertido em F°:{}'.format(C,F))