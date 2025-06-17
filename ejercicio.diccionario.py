#FUNCIONES Y DICCIONARIO
#Crear una funcion contar_ocurrenciad(palabras)
#que reciba una lista de palabras y retorne
#un diccionario con el contenido de cada una

def contar_ocurrencias(palabra):
    #definir el diccionario
    conteo={}
    for palabra in palabra:
        conteo[palabra] = conteo.get(palabra,0)+1
        
        return conteo

def main():
    
    lista_palabras=["hola","telefono","dos","holamundo"]
    resultado=contar_ocurrencias(lista_palabras)
    print(resultado)
if __name__=="__main__":
    main()
    
    