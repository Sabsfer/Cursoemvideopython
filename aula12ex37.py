num=int(input('Digite um número: '))
print('''Escolha uma das bases de conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL 
[3] converter para HEXADECIMAL''')
opção=int(input('Sua opção:'))
if opção==1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))#[2:] fatiamento para que fique somente o num e não aparece o tipo
elif opção==2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opção==3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('\033[31mOPÇÃO INVALIDA\033[m,\033[32mdigite novamente\033[m')