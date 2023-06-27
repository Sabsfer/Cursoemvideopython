somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
from time import sleep
for p in range(1,5):
    print('----- {}ª pessoa -----'.format(p))
    nome=str(input('NOME: ')).strip()
    idade=int(input('IDADE: '))
    sexo=str(input('SEXO (F/M): ')).strip()
    somaidade += idade 
    if p==1 and 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('\033[32mANALISANDO ...\033[m')
sleep(1)
print(' A média das idades do grupo é de {:.0f} anos'.format(mediaidade))
print('O homem mais velho é {} com {} anos'.format(nomevelho,maioridadehomem))
print('Foram informados um total de {} mulheres com menos de 20 anos'.format(totmulher))
        
        
