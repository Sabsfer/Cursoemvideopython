print('='*30)
print('  VERIFICADOR DE PALÍNDROMOS')
print('='*30)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#inverso = junto [::-1] opção sem precisar do for, e a var inverso  vazia
#pegou o inicio e o fim da frase ao contrario pelo -1
for letra in range (len(junto) -1, -1, -1):
    inverso +=junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')