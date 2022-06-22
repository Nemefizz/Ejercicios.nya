from numpy import matrix


def grabar():
    cant=0
    while(cant <= 10):
        parte = input("Ingrese numero de parte: \n")
        cant=len(parte)
        if cant<=10:
            print("Debe inresar un numero de parte de 10 caracteres o mas")
    cant=9
    while(cant <= 6):
        nombre = input("Ingrese nombre del parte: \n")
        cant=len(nombre)
        if cant<=10:
            print("Debe inresar un nombre de parte de 6 caracteres o mas")  
    
    while precio<=0:
        try:
            precio=int(input("Ingrese precio del producto:"))
            if precio <=0:
                print("EL precio debe ser mayor a 0")
        except:
            print("Debe ingresar un numero")
            precio=0
    lista = [[parte,nombre,precio]]
    return lista

def buscar(Matriz):
    cant=9
    while(cant <= 10):
        parte = input("Ingrese numero de parte: \n")
        cant=len(parte)
        if cant<=10:
            print("Debe inresar un numero de parte de 10 caracteres o mas")

    filas, columnas= Matriz.shape
    existe = False
    encontrada=0
    for fi in range(filas):
        if Matriz[fi][0]== parte:
            existe= True
            encontrada=fi
    if(existe):
        if Matriz[encontrada][2] >= 500:
            print(f"Parte: {Matriz[encontrada][0]}")
            print(f"Nombre: {Matriz[encontrada][1]}")
            print(f"Precio: {Matriz[encontrada][2]}")
        else:
            print("Producto sin stock")
    else:
        print("Producto no encontrado")
    def imprimir(Matriz):
        filas,columnas = matriz.shape
        for f in range(filas):
            print(f"{matriz[f][0]}  {matriz[f][1]}     {matriz[f][2]}")

