frase=str(input('Digite uma frase:')).lower().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('Ela aparece a primeira vez em {}'. format(frase.find('a')+1))
print('E a aparece a ultima vez em {}'.format(frase.rfind('a')+1))