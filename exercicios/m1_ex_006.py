'''
Conversor de temperaturas
Escreva um programa que converta uma temperatura
digitada em graus Celsius (C) e converta para graus Fahrenheit (F).

Assistir até a aula 07
'''
C=float(input('Informe-nos a temperatura em graus °C: '))
F=(C * 9/5)+32
print('{:.2f} °C, correspondem a  {:.2f} °F'.format(C, F))
C=(F-32)*5/9
print('{:.2f} °F, corresponde a {:.2f} °C'.format(F, C))
