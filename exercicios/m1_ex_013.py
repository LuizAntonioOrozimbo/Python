'''
Tocando um MP3

 Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

 Assistir até a aula-08
'''

import pygame  # importando a biblioteca pygame
pygame.init()  # Iniciando o pygame
pygame.mixer.music.load("Sultans_Of_Swing.mp3") # chamando a música
pygame.mixer.music.play() # dando play na música
input()
pygame.event.wait()
