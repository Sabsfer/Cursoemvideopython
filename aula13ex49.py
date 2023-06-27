print('-'*8)
print('TABUADA')
print('-'*8)
n=int(input('Digite um número: '))
for c in range (1,11):
    print('{} x {:2} = {}'.format(n,c,(n*c)))
