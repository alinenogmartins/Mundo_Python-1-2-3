''' Desafio Python 17:
Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.'''

print('='*30)
print('  CONTROLE DE VELOCIDADE')
print('='*30)

velocidade = float(input('Digite a velocidade do seu carro: '))
if velocidade > 80:
  multa = (velocidade - 80) * 5  
  print('\nMultado! Você excedeu o limite determinado que é de 80km/h.')      
  print(f'O valor da sua multa é de R${multa:.2f}')
else:  
  print('Parabéns, você está dentro do limite de velocidades....Dirija com segurança!\n')    
