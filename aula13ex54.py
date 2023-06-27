from datetime import date
totmenor=0
totmaior=0
cont=0
for pess in range (1,8):
    nasc = int(input('Qual o ano de nascimento da {} pessoa:'.format(pess)))
    atual=date.today().year
    idade=atual - nasc
    if idade <= 21 :
        totmenor += 1
    else:
        totmaior += 1
print(' Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('e também tivemos {} pessoas menores de idade'.format(totmenor))