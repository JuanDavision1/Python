import math
from decimal import Decimal
inf_positivo = float('inf')
#print(f'Infinito positvo  {inf_positivo}')
#print(f'Es infinito : {math.isinf(inf_positivo)}')
inf_negativo = float('-inf')
#print(f'infinito negativo {inf_negativo}')
#print(f'Es infinito : {math.isinf(inf_negativo)}')
##########modulo de math
inf_positivo= math.inf
#print(f'Infinito positvo  {inf_positivo}')
#print(f'Es infinito : {math.isinf(inf_positivo)}')
inf_negativo= -math.inf
#print(f'infinito negativo {inf_negativo}')
#print(f'Es infinito : {math.isinf(inf_negativo)}')

#######modulo decimal

inf_positivo= Decimal('Infinity')
print(f'Infinito positvo  {inf_positivo}')
print(f'Es infinito : {math.isinf(inf_positivo)}')

inf_negativo= Decimal('-Infinity')
print(f'infinito negativo {inf_negativo}')
print(f'Es infinito : {math.isinf(inf_negativo)}')