'''
Reajuste Salarial
Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento.

Assistir até a aula 07
'''
sal=float(input('Informe o salário do funcionário! R$'))
novosal=sal*1.15
print('O salário, é de R${:.2f} com 15% de aumento, passará a ser de R${:.2f}'.format(sal, novosal))
novosal=sal+(sal*15/100)
print('O salário, é de R${:.2f} com 15% de aumento, passará a ser de R${:.2f}'.format(sal, novosal))