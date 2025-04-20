'''
Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre: 
● O nome com todas as letras maiúsculas e minúsculas.
● Quantas letras ao todo (sem considerar espaços).
● Quantas letras tem o primeiro nome.

Assistir até a aula-09
'''
nome=str(input('Digite seu nome completo: ')).strip() # pede o nome ja eliminando os estacos antes e depois do nome.
print('Analisando seu nome...')

print()
print(f'Seu nome em maiusculas é: {nome.upper()}') # Nome ser'a impresso com todas as letras maiusculas
print() # Imprime uma linha em branco
print(f'Seu nome em minusculas e: {nome.lower()}') # Imprime o nome em Minusculas
print()
print(f'Seu nome tem ao todo {len(nome)-nome.count(" ")} letras')# Esta e uma forma
print(f'Seu primeiro nome tem {nome.find(" ")} letras') # atravéz do primeiro espaço, podemos calcular o numero de letras do primeiro nome

# OUTRA FORMA
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')