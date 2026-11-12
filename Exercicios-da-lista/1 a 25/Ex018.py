''' Desafio Python 18:
Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
dela e depois mostre se ela pode ou não votar.'''

from datetime import date

print(f'===== Ano de votação =====')
ano_nasc = int(input('Informe o ano que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc 
print(f'\nSua idade é {idade} anos.')
if idade >= 16:
    print('Parabéns você já pode votar. Vote com conciência!')
else:
    print('Tenha um pouco mais de paciência, você ainda não pode votar.')    