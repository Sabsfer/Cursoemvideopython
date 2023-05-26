salario = float(input('Qual o salário do funcionário? R$'))
if salario <= 1250.00:#menor ou igual
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganha R${:.2f} passará a ganhar R${:.2f}'. format(salario,novo))
