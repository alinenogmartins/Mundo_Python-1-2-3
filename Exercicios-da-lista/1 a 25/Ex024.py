''' Desafio Python 24:
Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e R$0.45 para viagens mais longas.'''

km = float(input('Digite quantos km deseja percorrer: '))
if km <= 200:
  valor = km * 0.50
  print(f'O valor da sua passagem será de R$ {valor}')
else:
  valor = km * 0.45
  print(f'O valor da sua passagem será R$ {valor}') 