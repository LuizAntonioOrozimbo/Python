'''
Conversor de moedas
Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos dólares ela pode comprar.
Conferir cotação do dolar
Cotação do dolar em 20 de Março de 2025 = 5.66

Assistir até a aula 07
'''

print('=^'*20)
dolar=5.66
real=float(input('Quantos dólares você tem na carteira? R$'))
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(real, real/dolar))

