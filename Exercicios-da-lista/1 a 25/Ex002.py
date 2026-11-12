'''Desafio Python 2:
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
Ex: Qual é o seu nome? João da Silva
Olá João da Silva, é um prazer te conhecer!'''

nome = str(input('Digite é seu nome: '))
print('Muito prazer em te conhecer, {} !'.format(nome))
