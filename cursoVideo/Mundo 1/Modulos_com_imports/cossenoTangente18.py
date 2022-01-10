#seno → sen α  = cateto oposto a α
#                  hipotenusa

#cosseno → cos α  = cateto adjacente a α
#                     hipotenusa

#tangente → tan α  =   cateto oposto a α     
#                    cateto adjacente a α
import math
angulo = float(input('Digite um valor de angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o SENO {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o COSSENO {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a TANGENTE {:.2f}'.format(angulo, tangente))

