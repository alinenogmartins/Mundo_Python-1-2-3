'''Desafio Python 12:
Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.'''

print('----------------------------')
print('      LEITOR DE PREÇO       ')
print('----------------------------')
print()
valorP = float(input('Digite o valor do produto? R$ '))
desconto = (valorP * 5) /100
print('Preço do produto atual R$ {}'.format(valorP))
print('| Preço do produto com 5% de desconto é R$ {:.2f} |'.format(valorP-desconto))