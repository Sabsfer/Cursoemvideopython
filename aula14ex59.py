from time import sleep
n1 =int(input('Primeiro valor:'))
n2=int(input('Segundo valor:'))
opção = 0
while opção != 5:
    print('OPÇÕES:')
    print('''[ 1 ] SOMAR 
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR 
[ 4 ] NOVOS NÚMEROS 
[ 5 ] SAIR DO PROGRAMA ''')
    opção=int(input('Qual a sua escolha? '))
    if opção == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1,n2,soma))
    elif opção == 2:
        produto =n1 * n2
        print('{} X {} = {}'.format(n1,n2,produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2 
            print('Entre os números {} e {} é maior o número {}'.format(n1,n2,maior))
    elif opção == 4:
        print('Informe os números novamente!')
        n1 =int(input('Primeiro valor:'))
        n2=int(input('Segundo valor:'))
    elif opção == 5:
        print('FINALIZANDO..')
    else:
        print('Opção inválida!')
    print('=+'*15)
    sleep(1)     
print('FIM do programa, volte sempre!')
            

            