#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
if __name__ == "__main__":
    i:int=1 #Se inicializa variable en 1.
    print ("números impares:")
    while i<=999: #Mientras que i sea menor o igual a 999...
        print (i) #Se imprime i.
        i+=2 #Se aumenta i de dos en dos para obtener solo los números impares.
    j:int=2 #Se inicializa variable en 2.
    print ("números pares:")
    while j<=1000: #Mientras que j sea menor o igual a 1000...
        print (j) #Se imprime j.
        j+=2 #Se va aumentando j de dos en dos para obtener solo los número pares.