print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
r1 = int(input('Qual o primeiro segmento?'))
r2 = int(input('Qual o segundo segmento?'))
r3 = int(input('Qual o terceiro segmento?'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 +r1:
    print('Esses segmentos de retas FORMAM um triangulo!')
else:
    print('Esses segmentos de retas NÃO FORMAM um triangulo')
