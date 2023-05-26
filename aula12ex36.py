print('-'*25)
print('   Empréstimo Bancário')
print('-'*25)
casa=float(input('Qual o valor da casa? R$ '))
salario=float(input('Salário do comprador ? R$'))
anos=int(input('Quantos anos de financiamento? '))
prestação=casa/(anos*12)
minimo=salario*30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos),end=' ')
print('a prestação será de R$ {:.2f}'.format(prestação))
if prestação>minimo:
    print('\033[31mEmpréstimo não pode ser concedido!\033[m ')
else:
    print('\033[32mEmpréstimo pode ser concedido!\033[m')