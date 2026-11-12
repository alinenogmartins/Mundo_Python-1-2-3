'''Desafio Python 16:
[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade
de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. 
Calcule quantos dias de vida um fumante perderá e exiba o total em dias.'''

cigarros_dias = int(input('Quantos cigarros você fuma por dia: '))
anos_fumante = int(input('A quantos anos você é fumante: '))

# primeira parte
total_cigarro_por_dias = cigarros_dias 
total_cigarro_por_anos = (total_cigarro_por_dias * 365) * anos_fumante
print(f"Por dia você fuma um total de {total_cigarro_por_dias} por dia.")
print(f'Até hoje você já fumou um total de: {total_cigarro_por_anos} cigarros.')

# segunda parte
#1440 minutos equivale a 24 horas * 60 minutos
total_perda_vida= (total_cigarro_por_anos*10)/1440
print(f"Você perdeu {total_perda_vida:.1f} dias de vida até hoje.") 