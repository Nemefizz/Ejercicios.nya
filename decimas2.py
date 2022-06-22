import numpy as np
from numpy import random
A=random.randint(0,301,(10))
B=random.randint(0,301,(10))
print(A)
print(B)
print(f"La suma de los elementos del arreglo A es {A.sum()}")
print(f"La suma de los elementos del arreglo B es {B.sum()}")
sum=0
for i in range(0,len(B)):
    if B[i] % 2 != 0:
        sum=sum+B[i]
acum=0
print(f"La suma de elementos impares es: {sum}")
for i in range(0,len(B)):
    if B[i] % 2 != 0:
        acum=acum+b[i]
acum=acum*b[i]
print(f"La multiplicacion de elementos impares es: {acum}")

