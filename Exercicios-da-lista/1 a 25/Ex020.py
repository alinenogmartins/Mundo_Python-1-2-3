'''Desafio Python 20:
Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.'''
 
num = int(input('Digite um qualquer: '))
resultado = num % 2
if resultado == 0:
  print(f'O número {num} é PAR!')
else:
  print(f'O número {num} é IMPAR')    