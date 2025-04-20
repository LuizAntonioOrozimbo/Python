# Somando dois números
# Crie um programa que leia dois números, e mostre a soma entre eles.

# Assistir até a aula 04

n1=int(input('Digite um número:'))
# Entrada do primeiro número convertido para inteiro, através da função int()

n2=int(input('Digite outro número:'))
# Entrada do segundo número convertido para inteiro
soma = n1 + n2
# Efetua a soma entre os números

print('A soma entre {} e {} é igual a: {}' .format(n1, n2, soma))
# Mostra o resultado de forma formatada

'''
Caso não precisemos da variável 'soma' mais para a frente, nem precisamos criá-la,
podemos fazer o cálculo diretamente no código ou dentro do format conforme abaixo.
'''
print('A soma entre {} e {} é igual a: {}'.format(n1, n2, n1+n2))
