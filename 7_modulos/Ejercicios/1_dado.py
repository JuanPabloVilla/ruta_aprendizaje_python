'''
Usa el módulo random

Simula el lanzamiento de un dado (número del 1 al 6)

Muestra "Lanzaste: [número]"
'''

from random import randint

dado = randint(1,6)

print(f"Lanzaste: {dado}")