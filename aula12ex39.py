from datetime import date
print('-'*20)
print('   ALISTAMENTO')
print('-'*20)
sexo=str(input('Qual o seu sexo? F ou M:')).upper()
if sexo=='F':
    print('Você é mulher, seu alistamento não é obrigatório!')
elif sexo=='M':
    print('Você é homem, seu alistamento é obrigatório!')
    nasc=int(input('Ano de nascimento:'))
    atual=date.today().year
    idade=atual - nasc
    print('Quem nasceu em {} tem {} anos em 2023.'.format(nasc, idade))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo=18-idade
        print('Ainda faltam {} anos para o seu alistamento'.format(saldo))
        ano=atual+saldo
        print('Seu alistamento será em {} '.format(ano))
    elif idade > 18:
        saldo=idade-18
        print('Você já deveria ter se alistado há {} anos'.format(saldo))
        ano=atual-saldo
        print('Seu alistamento foi em {}'.format(ano))
