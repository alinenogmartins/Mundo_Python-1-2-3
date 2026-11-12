'''Desafio Python 3:
Crie um programa que leia o nome e o salario de um funcionario, mostrando no final a msg.
Ex. Nome do Funcionário: Maria do Carmo/ Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.'''

from datetime import date

mes = date.today()
nome = str(input('Informe o nome: '))
sal = float(input('Informe o salário: '))
print(f'O funcionario(a) {nome} tem um sálario de R$ {sal:.2f} no mês {mes}.')
