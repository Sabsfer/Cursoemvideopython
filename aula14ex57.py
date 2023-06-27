sexo=str(input('Qual o seu sexo (F/M)? ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('\033[31mResposta invalida\033[m')
    sexo=str(input('Digite novamente: ')).strip().upper()[0]
print('seu sexo é {}'.format(sexo))