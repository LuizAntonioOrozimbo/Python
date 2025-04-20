'''
Catetos e Hipotenusa

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

Assistir até a aula 08
'''
import math
CO=float(input("Informe a medida do cateto oposto "))
CA=float(input("Informe a medida do cateto adjacente "))
HT=math.hypot(CO, CA)
print(f"A medida da hipotenusa é: {HT:.2f}")
print()
HT=(CO**2 + CA**2) **(1/2)
print(f"A hipotenusa é: {HT:.2f}")
print()
