'''
Aluguel de carros
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Assistir até a aula 07
'''
numdias=int(input('Quantos dias o carro foi alugado?'))
km=float(input('Quantos kilometros foram percorridos?'))
valorkm=km*0.15
aluguel=numdias*60
print('Por {} dias de aluguel, o valor será R${:.2f} e por {} kms rodados, serão pagos R${:.2f} num total de R${:.2f}'.format(numdias, aluguel, km, valorkm, aluguel+valorkm))


