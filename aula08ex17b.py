from math import hypot
co2=float(input('comprimento do cateto oposto:'))
ca2=float(input('comprimento do cateto adjacente:'))
hi2=hypot(ca2,co2)
print('hipotenusa é {:.2f}'.format(hi2))