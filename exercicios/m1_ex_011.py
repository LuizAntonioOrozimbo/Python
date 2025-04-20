'''
Sorteando um item na lista

Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

Assistir até a aula 08
'''
from random import choice
n1=str(input('Primeiro nome '))
n2=str(input('Segundo nome '))
n3=str(input('Terceiro nome '))
n4=str(input('Quarto nome '))
esco=choice([n1,n2,n3,n4])
print(f'O escolhido foi:{esco}')

