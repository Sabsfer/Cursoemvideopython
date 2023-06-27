resp='S'
soma=quant=media=maior=menor=0
while resp in 'Ss':
    num=int(input('Digite um número: '))
    soma+=num #vai receber e somar os números
    quant+=1 #contar a quantidade de números
    if quant == 1:#se não foi dado nenhum número logo ele é o maior e tbm o menor
        maior=menor=num
    else:
        if num > maior:#vai receber os numeros e verificar qual é o maior dos fornecidos
            maior=num
        if num < menor:
            menor=num
    resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]#transformar em maiusculas , tirar os espaços e usar a primeira letra que é por isso o zero
media=soma/quant #é colocado fora porque a media vai usar todos os valores juntos e não vai somando conforme é inserido
print('Foram informados {} números e sua média é {}'.format(quant,media))
print('O maior número informado é {} e o menor é {}'.format(maior,menor))
