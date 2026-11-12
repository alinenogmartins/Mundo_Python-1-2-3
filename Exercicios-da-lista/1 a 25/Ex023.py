''' Desafio Python 23:
Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. 
Faça um programa que leia nome sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
que: | Homens ganham 5% de desconto | Mulheres ganham 13% de desconto |'''

print('='* 30)
print('   FELIZ DIA DAS MULHERES   ')
print('='* 30)

nome = str(input('Informe seu nome: '))
sexo= str(input('Informe o sexo | M | ou |F | : ')).strip().upper()

if sexo == 'M' :
    valor = float(input('Informe o valor da compra: R$ '))
    desconto_masculino = (valor * 5) /100
    v_mas = valor - desconto_masculino
    print(f'Você ganhou 5% de desconto, o valor éR$ {v_mas}')
    
elif sexo == 'F':
    valor = float(input('Informe o valor da compra: R$ '))
    desconto_feminino = (valor * 13) /100
    v_fem = valor - desconto_feminino
    print(f'Você ganhou 13% de desconto, o valor é R$ {v_fem}')
    
else:
    print('Opção invalida, escolha opção M ou F')
    