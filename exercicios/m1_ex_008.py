'''
Quebrando um número

Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

Assistir até a aula 08
'''
from math import trunc

num=float(input('Digite um número real qualquer! '))
print(f"A parte inteira do número {num} é: {trunc(num)}")

