salario=float(input('Qual é seu salário?'))
nvsalario=salario+(salario*15/100)
aumento=salario*15/100
print('o salário do funcionario é {:.0f}, seu novo salário será {:.0f} com aumento de {:.0f}'.format(salario,nvsalario,aumento))