''' Desafio Python 22:
Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
situação em relação ao alistamento militar.
- Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
- Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.'''

#Importando ano atual
from datetime import date

print('__________________________')
print(' ALISTAMENTO MILITAR 2022 ')
print('__________________________')
ano_nasc=int(input("Informe o ano do seu nascimento: "))
atual = date.today().year
idade = atual - ano_nasc
print(f"Você tem {idade} anos de idade! \n")

#Ano do alistamento
if idade == 18:
  print("Esse é o ano do seu alistamento militar!")

# ainda vai se alistar
elif idade < 18:
  saldo = 18 - idade
  print(f"Ainda falta {saldo} anos para se alistamento militar.")
  ano = atual + saldo
  print(f'Seu alistamento será em {ano}')

#Ja alistado
elif idade > 18:
  saldo = idade - 18
  print(f"Você já deve ter se a alistado a {saldo} anos.")
  ano = atual - saldo
  print(f'Seu alistamento foi no ano {ano}!')