from math import radians,sin,cos,tan
ang=int(input('digite um angulo:'))
sen=sin(radians(ang))
print('o ângulo de {:.2f} tem o seno de {:.2f}:'.format(ang,sen))
cos=cos(radians(ang))
print('o ângulo de {:.2f} tem o cosseno de {:.2f}'.format(ang,cos))
tang=tan(radians(ang))
print('o angulo de {:.2f} tem a tangente {:.2f}'.format(ang,tang))