'''
Calculando descontos
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.

Assistir até a aula 07
'''
p=float(input('Informe o preço do produto! R$'))
np=p-p*0.05
print('O preço do produto é R${:.2f} o novo preço com 5% de desconto será de R${:.2f}'.format(p, np))
desc=p*5/100
print('O preço do produto é R${:.2f} o novo preço com 5% de desconto será de R${:.2f}'.format(p, p-desc))
