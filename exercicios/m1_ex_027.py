'''
Primeiro e último nome de uma pessoa

Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.

Assistir até a aula-09
'''
print()
NOME = str(input('Digite seu nome completo ')).strip()

print()
print(NOME)

print()
print(f'Seu primeiro nome é: {NOME[0:NOME.find(" ")]}')

print()
print(f'E seu último nome é:{NOME[NOME.rfind(" "):len(NOME)]}')
N = NOME[NOME.rfind(' ')+1: len(NOME)]
print('Prazer em conhecer',N)
print()

print('======== OUTRA FORMA ========')
NOME = NOME.split()

print(f'Seu primeiro nome é: {NOME[0]}')
print()

print(f'E seu último nome é: {NOME[len(NOME)-1]}')
print()
