from random import randint
from time import sleep
print('=+'*15)
print('     Jogo de adivinhação')
print('=+'*15)
print('JOGABILIDADE:\nVocê irá tentar adivinhar que número estou pensando entre 0 e 10 \nContarei suas tentativas')
computador=randint(0,10)
acertou = False
palpites = 0
while not acertou :
    jogador = int(input('Digite seu palpite:'))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Ainda não acertou, tente com mais')
            jogador = int(input('Digite seu palpite:'))
        if jogador > computador:
            print('Ainda não acertou, tente com menos')
            jogador = int(input('Digite seu palpite:'))
        print('Você acertou, PARABÉNS!!! foram precisas {} tentativas '.format(palpites))