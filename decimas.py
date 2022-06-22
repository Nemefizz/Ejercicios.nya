from array import array
import numpy as np
from numpy import random

arreglo1=np.array([["a","c","h","W"],['a','c','h','s'],['a','c','h','s'],['a','c','h','s']])
print(arreglo1)
vocales=0
consonantes=0
palabra=0

for f in range(4):
    for c in range(4):
        if (arreglo1[f][c] == "a" or arreglo1[f][c] == "e" or arreglo1[f][c] =="i" or arreglo1[f][c] =="o" or arreglo1[f][c] =="u"):
            vocales=vocales+1
        else: 
            consonantes=consonantes+1
print(f"cantidad de vocales: {vocales}")
print(f"cantidad de consonantes: {consonantes}")

