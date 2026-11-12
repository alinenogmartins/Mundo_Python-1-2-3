'''Desafio Python 25:
[DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
Analise seus comprimentos e diga se é possível formar um triângulo com essas retas. Matematicamente,
 para três segmentos formarem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois.''' 
 
print('=-'*20)
print('        AnaLisAdoR de TRianGuLo   ')
print('=-'*20)
primeiro = float(input('Digite o primeiro seguimento: '))
segundo = float(input('Digite o segundo seguimento: '))
terceiro = float(input('Digite o terceiro seguimento: '))

#Cada um dos seguimentos tem que ser menor que a soma dos outros dois
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
  print('Esses segmentos podem formar um TRIANGULO.')
  
  #– EQUILÁTERO: todos os lados iguais
  if primeiro == segundo == terceiro:
    print('Pode formar um triângulo: EQUILÁTERO!')
    
  #– ESCALENO: todos os lados diferentes
  elif primeiro != segundo != terceiro != primeiro:
    print('Pode formar um triângulo ESCALENO!')
    
  #– ISÓSCELES: dois lados iguais, um diferente
  else:
    print('Pode formar um triângulo: ISÓSCELES!')
else:
  print('Esses segmentos não podem formar um TRIANGULO!')
      