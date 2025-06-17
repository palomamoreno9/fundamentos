#FUNCIONES Y MATRICES

##Crear un funcion llamada sumar_filas(matriz) que reciba una matriz(lista de lista)
##de numeros y devuelva una lista con la suma de cada fila
def sumar_filas(matriz):
    
 return[sum(fila) for fila in matriz]

def main():
    #definimos matriz
    matriz=[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
    ]
    print("matriz")
    for fila in matriz:
        print(fila)
        
    resultado=sumar_filas(matriz)
    print("La suma  de cada fila es: ",resultado)

if __name__=="__main__":
    main()