print('=+'*12)
print('    GERADOR DE P.A')
print('=+'*12)
primeiro=int(input('Qual o primeiro termo? '))
razão=int(input('Qual a razão? '))
termo = primeiro
cont=1
while cont <= 10:
    print('{} - '.format(termo), end = ' ')
    termo += razão
    cont += 1
print('FIM!')
    
