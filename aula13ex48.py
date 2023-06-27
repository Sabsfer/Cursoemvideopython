somatot = cont = 0
for c in range (1,501,2):#intercalando de 2 em 2 é mostrados os impares
    if c % 3 == 0:#multiplos de 3
        somatot += c
        cont += 1
print('A soma total dos {} valores solicitados é {}'.format(cont,somatot))
