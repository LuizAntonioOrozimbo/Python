'''
Média Aritmética
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.

Assistir até a aula 07
'''

n1=float(input('informe a primeira nota!'))
n2=float(input('Informe a segunda nota!'))
media=(n1+n2)/2
print('A média do aluno é {:.2f}'.format(media)) # usando a variável
print('A média do aluno é {:.2f}'.format((n1+n2)/2)) # calculando direto no format
