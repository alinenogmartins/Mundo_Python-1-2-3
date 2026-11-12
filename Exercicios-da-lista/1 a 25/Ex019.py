''' Desafio Python 19:
Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela.
No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).'''

nome = input('Digite o nome do primeiro aluno: ')
primeira_nota = float(input('Informe a primeira nota: '))
segunda_nota = float(input('Informe a segunda nota: '))
media = (primeira_nota + segunda_nota) / 2
print(f'\nSua média é {media}')
if media >= 7.0:
    print('Parabéns!!! \nAprovado, ficou acima da média.')
if media < 7.0:
    print('Reprovado! Ficou abaixo da média.')    