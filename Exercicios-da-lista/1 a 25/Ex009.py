'''Desafio Python 09:
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

import requests

url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
requisicao = requests.get(url)

# A resposta vem em JSON, então vamos transformar em dicionário:
dados = requisicao.json()

# Acessa o valor da cotação do dólar (campo 'bid')
cotacao = float(dados['USDBRL']['bid'])

print('=-'*20)
print('        CONVERSOR DE MOEDAS        ')
print('=-'*20)
valor = float(input('Qual valor em reias você tem na carteira? R$ '))
dollar = valor / cotacao
print(f'Com R$ {valor} você poderá comprar U$ {dollar:.2f}')
print()
print(f'| Cotação do dia U$ {cotacao} |')

