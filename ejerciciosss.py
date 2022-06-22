import numpy as np
import ejerciciossfuncione as fu
lista=[["Parte","Nombre del producto","Precio del producto"]]
opcion = 0
matriz= np.array(lista)

while opcion != 4:  
    print("*********************************")
    print(" 1.-Grabar")
    print(" 2.-Buscar")
    print(" 3.-Imrimir")
    print(" 4.-Salir")
    print("*********************************")
    try:
        opcion = int(input("Ingresa tu opcion:"))
        
        if opcion == 1:
            lista2=fu.grabar()
            matriz=np.concatenate((matriz,lista2), axis=0)
        elif opcion == 2:
            fu.buscar(matriz)
        elif opcion == 3:
            print ("Opcion 3")
        elif opcion == 4:
            print ("Gracias por usar el sistema\nGenaro Espinoza")
        else:
            print ("Ingresa una opcion válida (Número del 1 al 4")
    except:
        print ("Ingresa una opcion válida (Número del 1 al 4")