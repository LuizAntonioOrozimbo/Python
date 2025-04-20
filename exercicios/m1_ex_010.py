'''
Seno, Cosseno e Tangente

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

Assistir até a aula 08
'''
from math import sin, cos, tan, radians
ang=float(input('Informe um ângulo '))
rad=radians(ang)
sen=sin(rad)
tang=tan(rad)
cosse=cos(rad)
print(f"O ângulo de {ang}°,\ntem como seno {sen:.2f},\ncomo cosseno {cosse:.2f}\ne a tangente {tang:.2f}")
