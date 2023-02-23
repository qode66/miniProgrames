"""
/*
 * Crea un generador de números pseudoaleatoris entre 0 i 100.
 * - No pots usar cap funció "random" (o semblant) del llenguatge de programació seleccionat.
 */
"""

import math
from datetime import datetime

#paràmetres de la funció de Gauss
sigma2 = 6.0
sigma = math.sqrt(sigma2)
mu = 0

def funcionGauss(x,s,m):

    a = 1 #altura de la campana, valor formal a = 1/(sigma*math.sqrt(2*math.pi))
    b = m #posicion del centro
    c = s #anchura de la campana

    y = a * math.exp(-((x - b)**2)/(2 * c**2)) #funcion de Gauss

    return y

dt = datetime.now()
seed = ((2*sigma2) * (dt.microsecond/1000000)) - sigma2

numAlea = round(100*(funcionGauss(seed,sigma,mu)))

print(numAlea)
