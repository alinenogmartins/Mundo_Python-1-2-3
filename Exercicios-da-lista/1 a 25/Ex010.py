''' Desafio Python 10:
Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a 
quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.'''

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
#Calculo da área da parede
area = altura * largura
print(f'A dimensão da área é {area:.2f} m²')
tinta = area/2
print(f'Você precisará de {tinta:.2f} litros de tinta para pintar essa determinada área.')
print()
print("__________________________________________________________________")
print("OBS: Cada litro de tinta pinta uma área de 2m²")