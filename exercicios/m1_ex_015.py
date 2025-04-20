'''
Separando dígitos de um número

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Assistir até a aula-09
'''
from random import randint
num = randint(0, 9999)
print(num)

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o número {num}...')
print()
print(f'O número {num} tem:\n{u} Unidades\n{d} Dezenas\n{c} Centenas\n{m} Milhar')


# PS.: Existe outra forma, que é usando estruturas de repetições