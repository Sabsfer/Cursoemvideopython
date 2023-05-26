v=float(input('Qual a velocidade atual do carro?'))
if v >80:
    print('Você foi multado por excede o limite que é 80KM!')
    multa=(v-80)*7
    print('Você deve pagar R${:.2f} de multa'.format(multa))
else:
    print('Tenha um excelente dia, dirija com cuidado!')

