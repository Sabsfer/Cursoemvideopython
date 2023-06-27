print ('-'*10)
print ('  MÉDIAS')
print ('-'*10)
print ('Olá, vamos calcular sua média')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
print ('A primeira nota é {}\nA segunda nota é {}'.format(nota1,nota2))
media = nota1+nota2/2
print('Média: {}'.format(media))
if media >7:
    print('\033[31mAPROVADO!!!\033[m')


