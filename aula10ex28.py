from random import randint #sorteio de número inteiros
from time import sleep
computador=randint(0,5) #faz o computador "pensar"
print('-=-'*20)
print('Vou pensar em um número tente adivinhar..')
print('-=-'*20)
jogador=int(input('Em que número eu pensei?'))#jogador tenta adivinhar
print('PROCESSANDO..')
sleep(2)#coloca o computador para aguardar os segundos que foi inserido antes da prox resposta
if jogador==computador:
    print('Você ganhou, parabéns')
else:
    print('Eu ganhei! Pensei no número {} e não no {}'.format(computador,jogador))

