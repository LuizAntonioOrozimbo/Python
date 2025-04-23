'''
Primeira e última ocorrência de uma string

Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez
e em que posição ela aparece a última vez.

Assistir até a aula-09
'''
print()  # imprime uma linha em branco
# Cria a frase, eliminando possíveis espaços no início e no fim da mesma
FRASE = str(input('Digite uma frase ')).strip()

print()  # Uma linha em branco
print(FRASE)  # imprime a frase
print()  # Uma linha em branco

print(f'Nossa frase tem {FRASE.upper().count("A")} letras "A"')
'''
O print acima, Joga a frase para caixa alta e
conta quantas letras 'A' tem na frase, porém,
ela não conta as letras acentuadas
'''

print()
print(f'A primeira letra "A", aparece na {FRASE.upper().find("A")+1}ª posição')
''' O print acima, Joga a frase para caixa alta e
mostra em que posição a primeira letra 'A' aparece na frase.
print()
'''
print()

print(f'A última letra "A", aparece na {FRASE.upper().rfind("A")+1}ª posição')
print()
