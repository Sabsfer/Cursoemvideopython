dias=int(input('por quantos dias foi alugado?'))
km=float(input('quantos kilômetros foram rodados?'))
aluguel=(dias*60)+(km*0.15)
print ('o total a pagar pelo aluguel é R${:.2f}'.format(aluguel))