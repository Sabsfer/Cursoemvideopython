print('=+'*10)
print('GERADOR DE P.A')
print('=+'*10)
primeiro=int(input('Qual o primeiro termo? '))
razão=int(input('Qual a razão? '))
termo = primeiro
c=1
total = 0 
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -'.format(termo), end =' ')
        c +=1
        termo += razão
    print('PAUSA')
    mais=int(input('Gostaria que fosse exibido mais quantos termos? '))
print('Foram exibidos {} termos'.format(total))
        
