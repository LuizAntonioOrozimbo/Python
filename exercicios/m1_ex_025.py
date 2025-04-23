'''
Procurando uma string dentro de outra

Crie um programa que leia o nome de uma pessoa
e diga se ela tem "SILVA" no nome.

Assistir até a aula-09

'''

nome = str(input('Digite seu nome completo ')).upper().strip().split()

print(f'Seu nome tem Silva? {'SILVA' in nome}')
