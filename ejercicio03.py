#FUNCIONES Y TUPLAS

#Escribir una funcion mayor_y_menor(tupla_numeros) que reciba una tupla con numeros y retorne el numero mayor y menor como tupla
def mayor_y_menor(tupla):
    return(max(tupla),min(tupla))
def main():
    tupla=(7,5,3,9,8,10,1.2,4,6,2,75)
    print(tupla)
    resultado=mayor_y_menor(tupla)
    print(resultado)
    

if __name__=="__main__":
    main()                                     