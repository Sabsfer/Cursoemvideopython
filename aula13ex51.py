#MINHA SOLUÇÃO
print('='*25)
print('   10 TERMOS DE UMA PA')
print('='*25)
primeiro = int(input('Qual o primeiro termo ? '))
razao = int(input('Qual a razão? '))
n = 11
ultimo = primeiro + (n-1) * razao
for c in range (primeiro,ultimo,razao):
    print(c, '-' ,end=' ')
print('ACABOU')

#SOLUÇÃO DO GUANABARA
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10-1) * razão
for c in range (primeiro, decimo + razão, razão):
    print('{}'.format(c),end='-')
print('ACABOU')
