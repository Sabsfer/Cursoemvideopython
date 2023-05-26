numero=int(input('Diga um número?'))
resultado=numero%2 #o resto da divisão de qualquer numero par por 2 é zero e o resto da divisão de qualquer numero impar é 1
if resultado==0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))