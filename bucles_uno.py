#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
def cuadrado (i:int)->int: #función para obtener el cuadrado de un número, recibe y devuelve un entero.
    potencia=i**2 #Se calcula la potencia del número recibido.
    return potencia #Se devuelve el cuadrado del número.
if __name__ == "__main__":
    i:int=1 #Se inicializa variable en 1.
    while i<=100: #Mientras que i sea menor o igual a 100...
        print ("NÚMERO:",i,"- CUADRADO:",cuadrado(i)) #Se imprime el número y se evalúa la función 'cuadrado' con número y el resultado se imprime.
        i+=1 #Se suma 1 a i para pasar al siguiente número.