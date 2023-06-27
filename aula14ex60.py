#from math import factorial
#n = int (input('Digite um número: '))
#f = factorial(n)
#print('O fatorial de {} é {}'.format(n,f))
#forma de calcular com a biblioteca mas nem todas as linguagens tem essa biblioteca
#n = int (input('Digite um número para calcular seu fatorial: '))
#c = n
#f = 1

#print('Calculando {}!'.format(n),end = ' ')
#while c > 0:
    #print('{}'.format(c) ,end = ' ')
    #print('x' if c > 1 else '=', end = ' ')
    #f *= c
    #c -= 1
#print(f)
#forma usando while que é a forma que pode ser usada em outras linguagens

n = int (input('Digite um número para calcular seu fatorial: '))
f = 1
print(f'{n}!' ,end = ' ')
for c in range(n, +1, -1):
    print(f'{c} x', end = ' ')
    f *= c
print (f"1 = {f}")