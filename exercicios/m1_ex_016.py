'''
Verificando as primeiras letras de um texto

Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

Assistir até a aula-09
'''
print('Resolução do Curso em Vídeo')
print()
cid = str(input('Em que cidade você nasceu? ')).strip()
print()
print(cid[:5].upper() == 'SANTO')
