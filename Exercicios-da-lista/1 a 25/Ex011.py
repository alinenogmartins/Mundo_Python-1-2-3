''' Desafio Python 11:
Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.'''

print('='*30)
print('  CÁLCULO DO DELTA')
print('='*30)

# Lê os valores de A, B e C
a = float(input('Informe o valor de A: '))
b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))

# Calcula o delta
delta = b**2 - 4 * a * c

# Exibe o resultado
print(f'O valor de Δ (delta) é: {delta}')
