'''Desafio Python 15:
Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário,
sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.'''

dias_trabalhados = int(input('Digite os dias trabalhados no mês corrente: '))
valor_dia = 8 * 25 #200,00/dia 
salario = dias_trabalhados * valor_dia
print(f'O seu salário esse mês é R$ {salario} ref. a {dias_trabalhados} dias trabalhado esse mês.')