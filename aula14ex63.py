print('='*30)
print('  SEQUÊNCIA DE FIBONACCI')
print('='*30)
n=int(input('Qual o número de elementos para a sequência? '))
t1=0
t2=1
cont = 3
print('{}->{}'.format(t1,t2), end = ' ')
while cont <= n:
    t3 = t1 + t2
    print('->{}->'.format(t3), end = ' ')
    cont += 1
    t1 = t2
    t2 = t3
print('FIM!')


    