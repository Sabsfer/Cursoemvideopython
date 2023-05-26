from datetime import date
ano=int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano==0:
    ano=date.today().year#mostra o ano atual da maquina
if ano%4==0 and ano%100!=0 or ano%400==0:#se o ano for divisivel por 4 ou seja o resto da divisão for zero
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))