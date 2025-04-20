'''
Pintando parede
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

Assistir até a aula 07
'''
larg=float(input('Informe-nos a largura da parede em metros!'))
alt=float(input('Informe-nos a altura da parede em metros!'))
print('A parede tem {} m², e para pintá-la, serão necessários {} litros de tinta.'.format(larg*alt, larg*alt/2))
print('=^='*20)

a=larg*alt
l=a/2
print('A parede tem {} m². Para pintá-la, precisaremos de {} litros de tinta'.format(a, l))