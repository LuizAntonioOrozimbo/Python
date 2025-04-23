'''
Conversor de medidas
Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milímetros.

Assistir até a aula 07
'''
m=float(input('Informe a metragem!'))
cm=m*100
mm=m*1000
print('{} metros, tem {} centímetros e {} milímetros'.format(m, cm, mm))

# Fazer também para km, hm, dam, m, dm, cm, mm

km=m/1000
hm=m/100
dam=m/10
dm=m*10

print("{0} metros, correspondem a: {1} km, {2} hm, {3} dam e {4} dm.".format(m, km, hm, dam, dm))
