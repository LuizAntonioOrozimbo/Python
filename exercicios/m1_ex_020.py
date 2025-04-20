'''
Dissecando uma variável
Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.

Assistir até a aula 06
'''
n1=str(input('Digite algo!'))
print(type(n1))
print('({}) pode ser alfanumérico? {}'.format(n1,n1.isalnum()))
print('({}) é alfabético? {}'.format(n1, n1.isalpha()))
print('({}) pode ser digito? {}' .format(n1, n1.isdigit()))
print('({}) está em minúsculas? {}' .format(n1, n1.islower()))
print('({}) pode ser decimal? {}'.format(n1, n1.isdecimal()))
print('({}) pode ser um identificador? {}'.format(n1, n1.isidentifier()))
print('({}) pode ser imprimível? {}'.format(n1, n1.isprintable()))
print('({}) é composto de espaços? {}'.format(n1, n1.isspace()))
print('({}) está capitalizado? {}'.format(n1, n1.istitle()))
print('({}) está em maiúsculas? {}'.format(n1, n1.isupper()))
print('({}) pode ser numérico? {}'.format(n1, n1.isnumeric()))
#print(n1.isascii())

