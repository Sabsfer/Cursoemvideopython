distancia=float(input('Qual a distância?'))
print('Você vai fazer uma viagem de {} Km..'.format(distancia))
if distancia<200:
    preco= distancia * 0.5
    print('Sua viagem custará R${:.2f}'.format(preco))
else:
    preco=distancia*0.45
    print('Sua viagem custará R${:.2f}'.format(preco))
