'''
Radar eletrônico

 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

Assistir até a aula-10
'''
print()
print(f'<=>' * 29)
print(f'{" RADAR ELETRÔNICO " :=^87}')
print(f'<=>' * 29)
print()
vel = float(input('Informe a velocidade! '))
print()
if vel <= 80:
    print('PARABÉNS!\nVocê está dentro do limite de velocidade permitido')
else:
    print(f'MULTADO!!!\n A velocidade permitida é de 80 Km/h\n Sua velocidade foi {vel}Km/h\n O valor da sua multa é R$ {(vel - 80) * 7 :.2f}')
# print(f'{vel:.2f} Km/h')
print()
print(f'{" FIM ":=^87}')
print()

# RESOLUÇÃO DO CURSO EM VÍDEO
print(f'{" RESOLUÇÃO DO CURSO EM VÍDEO ":=^87}')
print()

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!' .format(multa))
print('Tenha um bom dia! Dirija com segurança!')

print(f'{" FIM ":=^87}')
print()

# Foi utilizado apenas um if sem else o que chamamos de condição SIMPLES
