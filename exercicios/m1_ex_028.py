'''
Jogo da Adivinhação v.1.0

 Escreva um programa que faça o computador “pensar”
 em um número inteiro entre 0 e 5 e peça para o usuário
 tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.

Assistir até a aula-10
'''
from random import randint
from time import sleep

num = randint(0, 5)
esc = int(input('Digite um número de 0 a 5 '))
if num != esc:
    print(f'Você escolheu {num} e eu sorteei {esc}. QUE PENA, VOCÊ PERDEU!')
else:
    print(f'Você escolheu {num} e eu sorteei {esc}. PARABÉNS, VOCÊ VENCEU!')

# Resolução do Curso em Vídeo

computador = randint(0, 5)
# Faz o computador "PENSAR" em um número entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2)  # espera por dois segundos antes de continuar

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')
